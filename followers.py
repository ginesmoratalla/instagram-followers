import instaloader
import getpass

print("""
  (_)__  ___ / /____ ____ ________ ___ _    / _/__  / / /__ _    _____ _______
 / / _ \(_-</ __/ _ `/ _ `/ __/ _ `/  ' \  / _/ _ \/ / / _ \ |/|/ / -_) __(_-<
/_/_//_/___/\__/\_,_/\_, /_/  \_,_/_/_/_/ /_/ \___/_/_/\___/__,__/\__/_/ /___/
""")

print("Logging in, please wait...\n")

# Instaloader instance
Loader = instaloader.Instaloader()

while True:

    # User credentials
    username = input("Please enter your username: ")
    password = getpass.getpass("Please enter your password: ")

    # Try login
    try:
        Loader.login(username, password)
        print("\nLogin successful, loading profile details...\n")
        break

    except instaloader.exceptions.BadCredentialsException:
        print("Invalid credentials. Check your username and/or password.\n")
    except Exception as e:
        print("Unexpected error during login:", str(e))

    print("Please, try again.\n")


# Get profile information
profile = instaloader.Profile.from_username(Loader.context, username)

# Print the number of followers and people this account follows
print(f"{username} has {profile.followers} followers")
print(f"{username} follows {profile.followees} people\n")
print(f"Checking the people who do not follow {username}, it might take some time...\n")

# Get a list of followers and people this account follows
followers = [follower.username for follower in profile.get_followers()]
followees = [followee.username for followee in profile.get_followees()]

for x in followees:
    if x not in followers :
        print(f"{x} does not follow you back!")

