from rest_framework import generics
from userAuth_app.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
import random
from django.contrib.auth.models import Group
from django.conf import settings
from project_api .models import Project 
from rest_framework.decorators import action
from rest_framework.views import APIView
from .serializers import userAuthSerializers
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
import logging
from django.conf import settings
from .models import LDAPGroup, LDAPGroupMember,ADGroupRoleAssignment
import ldap
from django.http import JsonResponse
from .models import LDAPGroup, LDAPGroupMember
import urllib.parse
from django_auth_ldap.backend import LDAPBackend
from rest_framework.decorators import action
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from userAuth_app.permissions import IsAllowedRole
from rest_framework.authentication import TokenAuthentication
from .serializers import UserRoleSerializer,userAuthSerializers,UserListSerializer,UserRoleSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes

user_creation_logger = logging.getLogger('user_creation_logger')
class UserRegistrationView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAllowedRole]

    def generate_random_project_name(self):
        static_prefix = "default-"
        adjectives = ['happy', 'colorful', 'creative', 'vibrant', 'sparkling']
        nouns = ['unicorn', 'rainbow', 'garden', 'ocean', 'harmony']
        random_adjective = random.choice(adjectives)
        random_noun = random.choice(nouns)
        generated_name = f"{static_prefix}{random_adjective}-{random_noun}"
        while Project.objects.filter(project_name=generated_name).exists():
            random_adjective = random.choice(adjectives)
            random_noun = random.choice(nouns)
            generated_name = f"{static_prefix}{random_adjective}-{random_noun}"
        return generated_name

    def post(self, request):
        serializer = userAuthSerializers(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.save()

            # Assign random project to the user
            project_name = self.generate_random_project_name()
            project = Project.objects.create(user=user, project_name=project_name)

             # Log the user creation
            log_entry = f"user={user.username} project={project_name} msg={user.username} created"
            user_creation_logger.info(log_entry)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


login_logger = logging.getLogger('login_logger')
class UserLoginView(ObtainAuthToken):
    authentication_classes = [TokenAuthentication]
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        print(f'{username} and {password}')

        user = authenticate(request, username=username, password=password)
        print("user", user)
        if user is not None:
            login(request, user)

             # Retrieve user's role
            user_role = user.role if hasattr(user, 'role') else 'undefined'
            log_entry = f"user={user.username} role={user_role} msg=logged in"
            login_logger.info(log_entry)
            token, created = Token.objects.get_or_create(user=user)
            if created:
                token.delete()  # Delete the token if it was already created
                token = Token.objects.create(user=user)
            return Response({'token': token.key, 'username': user.username, 'role': user.role})
        else:
            return Response({'message': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)


login_logger = logging.getLogger('login_logger')
class LoginViewSet(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]

    def create(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username is None or password is None:
            return Response({"error": "Please provide both username and password"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(username=username).first()
        

        if user is not None and user.check_password(password):
            # Authenticate user
            user = authenticate(request, username=username, password=password)

            if user:
                # Log the user in
                login(request, user)

                # Log the login event
                user_role = user.role if hasattr(user, 'role') else 'undefined'
                log_entry = f"user={user.username} role={user_role} msg=logged in"
                login_logger.info(log_entry)

                # Generate or get token
                token, created = Token.objects.get_or_create(user=user)
                if created:
                    token.delete()  # Delete the token if it was already created
                    token = Token.objects.create(user=user)

                # Serialize user data
                serializer = userAuthSerializers(user)
                return Response({'token': token.key, 'user_data': serializer.data, 'role': user.role})

        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_details(request):
    user = request.user
    return Response({
        'username': user.username,
        'email': user.email,
        # add other details as needed
    })

# User role view
class UserRoleView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserRoleSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
logout_logger = logging.getLogger('logout_logger')
class UserLogoutView(APIView):
    authentication_classes = [TokenAuthentication]   
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user = request.user
        token_key = request.auth.key
        token = Token.objects.get(key=token_key)
      
        token.delete()
        # Log the user logout event
        log_entry = f"user={user.username} msg=logged out"
        logout_logger.info(log_entry)

        return Response(status=204)

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAllowedRole]  

login_logger = logging.getLogger('login_logger')
class LDAPLoginView(ObtainAuthToken):
    authentication_classes = [TokenAuthentication]

    def generate_random_project_name(self):
        static_prefix = "default-"
        adjectives = ['happy', 'colorful', 'creative', 'vibrant', 'sparkling']
        nouns = ['unicorn', 'rainbow', 'garden', 'ocean', 'harmony']
        random_adjective = random.choice(adjectives)
        random_noun = random.choice(nouns)
        generated_name = f"{static_prefix}{random_adjective}-{random_noun}"
        while Project.objects.filter(project_name=generated_name).exists():
            random_adjective = random.choice(adjectives)
            random_noun = random.choice(nouns)
            generated_name = f"{static_prefix}{random_adjective}-{random_noun}"
        return generated_name

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate using LDAPBackend
        ldap_backend = LDAPBackend()
        user = ldap_backend.authenticate(request, username=username, password=password)

        if user is not None:
            # Check if the user is active
            if not user.is_active:
                return Response({'error': 'This user is inactive'}, status=status.HTTP_401_UNAUTHORIZED)

            # Log the user in
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')

            # Retrieve user's role
            user_role = user.role if hasattr(user, 'role') else 'undefined'
            log_entry = f"user={user.username} role={user_role} msg=logged in"
            login_logger.info(log_entry)

            # Check if the user already has a project assigned
            existing_project = Project.objects.filter(user=user).first()

            if existing_project:
                # User already has a project assigned
                project_name = existing_project.project_name
            else:
                # Generate a random project name and assign it to the user
                project_name = self.generate_random_project_name()

                # Create a new project and associate it with the user
                Project.objects.create(user=user, project_name=project_name)
            
            # Generate or retrieve token for the user
            token, created = Token.objects.get_or_create(user=user)

            # Return response with token, username, role, and project name
            return Response({
                'token': token.key,
                'username': user.username,
                'role': user.role,
                'project_name': project_name
            })

        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_ADgroup_users(request):
    try:
        # Fetch LDAP configuration from settings
        ldap_server_uri = settings.AUTH_LDAP_SERVER_URI
        bind_dn = settings.AUTH_LDAP_BIND_DN
        bind_password = settings.AUTH_LDAP_BIND_PASSWORD
        search_base_groups = 'CN=Users,DC=os3,DC=com'
        search_filter_groups = "(objectClass=group)"
        
        # Establish LDAP connection
        ldap_connection = ldap.initialize(ldap_server_uri)
        ldap_connection.simple_bind_s(bind_dn, bind_password)

        # Search for all groups
        ldap_groups = ldap_connection.search_s(
            search_base_groups,
            ldap.SCOPE_SUBTREE,
            search_filter_groups,
            ['sAMAccountName', 'member']
        )

        # Iterate over LDAP groups
        for dn, entry in ldap_groups:
            group_name = entry.get('sAMAccountName', [])[0].decode('utf-8')
            print("group_name", group_name)

            # Check if the group already exists in the database
            ldap_group, created = LDAPGroup.objects.get_or_create(name=group_name)

            # Retrieve and save member sAMAccountName
            members = entry.get('member', [])
            for member in members:
                member_dn = member.decode('utf-8')
                # Fetch the member's sAMAccountName
                member_info = ldap_connection.search_s(
                    member_dn,
                    ldap.SCOPE_BASE,
                    '(objectClass=*)',
                    ['sAMAccountName']
                )
                if member_info:
                    member_name = member_info[0][1].get('sAMAccountName', [])[0].decode('utf-8')
                    print("member_name", member_name)
                    # Save group member if not already exists
                    LDAPGroupMember.objects.get_or_create(group=ldap_group, username=member_name)

        return JsonResponse({'message': 'LDAP groups and members saved successfully'})

    except ldap.LDAPError as e:
        return JsonResponse({'error': str(e)}, status=500)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsAllowedRole])
def list_ad_groups_with_members(request):

    try:
        # Establish LDAP connection
        ldap_server_uri = settings.AUTH_LDAP_SERVER_URI
        bind_dn = settings.AUTH_LDAP_BIND_DN
        bind_password = settings.AUTH_LDAP_BIND_PASSWORD
        ldap_connection = ldap.initialize(ldap_server_uri)
        ldap_connection.simple_bind_s(bind_dn, bind_password)

        # Search for all groups
        search_base_groups = 'CN=Users,DC=os3,DC=com'
        search_filter_groups = "(objectClass=group)"
        ldap_groups = ldap_connection.search_s(
            search_base_groups,
            ldap.SCOPE_SUBTREE,
            search_filter_groups,
            ['sAMAccountName', 'member']
        )

        group_info = []

        for dn, entry in ldap_groups:
            group_name = entry.get('sAMAccountName', [])[0].decode('utf-8')
            members = entry.get('member', [])
            member_names = []

            for member in members:
                member_dn = member.decode('utf-8')
                # Fetch the member's sAMAccountName
                member_info = ldap_connection.search_s(
                    member_dn,
                    ldap.SCOPE_BASE,
                    '(objectClass=*)',
                    ['sAMAccountName']
                )
                if member_info:
                    member_name = member_info[0][1].get('sAMAccountName', [])[0].decode('utf-8')
                    member_names.append(member_name)

            group_info.append({
                'group_name': group_name,
                'members': member_names
            })

        return JsonResponse({'groups': group_info}, safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsAllowedRole])
def save_ad_users(request):
    try:
        # Establish LDAP connection
        ldap_server_uri = settings.AUTH_LDAP_SERVER_URI
        bind_dn = settings.AUTH_LDAP_BIND_DN
        bind_password = settings.AUTH_LDAP_BIND_PASSWORD
        
        ldap_connection = ldap.initialize(ldap_server_uri)
        ldap_connection.simple_bind_s(bind_dn, bind_password)
        
        # Search base and filter
        search_base = 'CN=Users,DC=os3,DC=com'
        search_filter = "(objectClass=user)"  # Filter to retrieve all users
        
        # Specify attributes to retrieve
        attributes = ['sAMAccountName']  # Only retrieving sAMAccountName
        
        # Search for users
        ldap_users = ldap_connection.search_s(
            search_base,
            ldap.SCOPE_SUBTREE,
            search_filter,
            attributes
        )
        
        # Extract sAMAccountName and save to the database
        user_data = []

        for dn, entry in ldap_users:
            if 'sAMAccountName' in entry:
                sam_account_name = entry['sAMAccountName'][0].decode('utf-8')
                # Save the sAMAccountName to the User model if not already present
                if not User.objects.filter(username=sam_account_name).exists():
                    User.objects.create(username=sam_account_name)
                user_data.append({'sAMAccountName': sam_account_name})
        
        return JsonResponse({'users': user_data}, safe=False)
    
    except ldap.LDAPError as e:
        return JsonResponse({'error': str(e)}, status=500)
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


role_assignment_logger = logging.getLogger('role_assignment_logger')
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsAllowedRole])
def assign_or_change_role(request, username):
    try:
        user = User.objects.get(username=username)
        role = request.data.get('role')

        if role not in dict(User.ROLE_CHOICES).keys():
            return Response({'error': 'Invalid role'}, status=status.HTTP_400_BAD_REQUEST)

        user.role = role
        user.save()
        # Log the role assignment event
        log_entry = f"user={user.username} msg=Role changed to: {role}"
        role_assignment_logger.info(log_entry)

        return Response({'message': f'Role for {username} changed to {role}'}, status=status.HTTP_200_OK)

    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


class UserRoleAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
            serializer = UserRoleSerializer(user)
            return Response({'role': serializer.data['role']}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

Grouprole_assignment_logger = logging.getLogger('Grouprole_assignment_logger')
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsAllowedRole])
def assign_roles_to_adgroup_members(request):
    if request.method == 'POST':
        group_name = request.data.get('group_name')
        role_name = request.data.get('role_name')
        sAMAccountNames = request.data.get('sAMAccountNames')

        if not group_name or not role_name or not sAMAccountNames:
            return Response({'success': False, 'message': 'group_name, role_name, and sAMAccountNames are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Find the group object
            group = LDAPGroup.objects.get(name=group_name)

            # Find the group members
            group_members = LDAPGroupMember.objects.filter(group=group)

            # Assign the new role to each user
            for member in group_members:
                user, _ = User.objects.get_or_create(username=member.username)
                user.role = role_name  # Assuming you can directly set the role field
                user.save()

            # Create or update ADGroupRoleAssignment
            ad_group_assignment, _ = ADGroupRoleAssignment.objects.update_or_create(
                group_name=group_name,
                defaults={'role_name': role_name}
            )

            log_entry = f"group={group_name}, role={role_name}, msg=role assign to group, sAMAccountNames={sAMAccountNames}"
            Grouprole_assignment_logger.info(log_entry)

            return Response({'success': True, 'message': f'Roles assigned to members of {group_name}'})
        except LDAPGroup.DoesNotExist:
            log_entry = f"msg=Failed role assignment group_name={group_name} reason=Group does not exist"
            Grouprole_assignment_logger.info(log_entry)
            return Response({'success': False, 'message': f'Group {group_name} does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            log_entry = f"msg=Failed role assignment group_name={group_name} reason={str(e)}"
            Grouprole_assignment_logger.error(log_entry)
            return Response({'success': False, 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response({'success': False, 'message': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsAllowedRole])
def get_adgroup_role(request, group_name):
    try:
        # Decode the group name
        decoded_group_name = urllib.parse.unquote(group_name)
        
        # Fetch the AD group role assignment
        ad_group_role_assignment = ADGroupRoleAssignment.objects.get(group_name=decoded_group_name)
        role_name = ad_group_role_assignment.role_name
        return Response({'success': True, 'group_name': decoded_group_name, 'role_name': role_name})
    except ADGroupRoleAssignment.DoesNotExist:
        return Response({'success': False, 'message': f'No role assigned to group {decoded_group_name}'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class IsConnectedAPIView(APIView):
    # authentication_classes = [TokenAuthentication]   
    # permission_classes = [IsAuthenticated,IsAllowedRole]
    def get(self, request):

        is_connected = settings.IS_CONNNECTED.strip()  # Corrected attribute name and stripping whitespace
        print("is_connected", is_connected)
        return Response({'is_connected': is_connected})

from django.contrib.auth import get_user_model

User = get_user_model()

class CreateFirstAdminAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # Check if there are any existing admin users
        if User.objects.filter(is_superuser=True).exists():
            return Response({'error': 'Admin user already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create the first admin user
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        role = request.data.get('role')
        if not username or not password:
            return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        admin_user = User(username=username, role=role, email=email, is_superuser=True, is_staff=True)
        admin_user.set_password(password)
        admin_user.save()
        
        return Response({'success': 'Admin user created successfully.'}, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        return Response({'error': 'GET method is not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
def check_admin_user_exists(request):
    if User.objects.filter(is_superuser=True).exists():
        return JsonResponse({'exists': True})
    return JsonResponse({'exists': False})



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userAuthSerializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated , IsAllowedRole]

    @action(detail=False, methods=['patch'], url_path='toggle-status')
    def toggle_user_status(self, request, username=None):
        try:
            user = get_object_or_404(User, username=username)
            user.is_active = not user.is_active
            user.save()
            status_message = 'user enabled' if user.is_active else 'user disabled'
            return Response({'status': status_message}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=False, methods=['get'], url_path='status/(?P<username>[^/.]+)')
    def get_user_status(self, request, username=None):
        try:
            user = get_object_or_404(User, username=username)
            return Response({'is_active': user.is_active}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordView(APIView):
    def post(self, request, username):
        user = get_object_or_404(User, username=username)
        new_password = request.data.get('new_password')
        if not new_password:
            return Response({"error": "New password is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        user.set_password(new_password)
        user.save()
        return Response({"message": "Password has been reset successfully."}, status=status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userAuthSerializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated , IsAllowedRole]

    @action(detail=False, methods=['patch'], url_path='toggle-status')
    def toggle_user_status(self, request, username=None):
        try:
            user = get_object_or_404(User, username=username)
            user.is_active = not user.is_active
            user.save()
            status_message = 'user enabled' if user.is_active else 'user disabled'
            return Response({'status': status_message}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=False, methods=['get'], url_path='status/(?P<username>[^/.]+)')
    def get_user_status(self, request, username=None):
        try:
            user = get_object_or_404(User, username=username)
            return Response({'is_active': user.is_active}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordView(APIView):
    def post(self, request, username):
        user = get_object_or_404(User, username=username)
        new_password = request.data.get('new_password')
        if not new_password:
            return Response({"error": "New password is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        user.set_password(new_password)
        user.save()
        return Response({"message": "Password has been reset successfully."}, status=status.HTTP_200_OK)
