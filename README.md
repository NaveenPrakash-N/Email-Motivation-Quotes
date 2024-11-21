# Email-Motivation-Quotes
A Python script to send random motivational quotes via email. Reads quotes from a file, selects one at random, and sends it using SMTP. Users securely input their email, app password, and recipient's address. Ideal for learning Python email automation and sharing daily inspiration.


How to Generate and Use a Google App Password
If you're using Gmail to send emails through your Python script, you’ll need to generate an App Password if you have 2-Step Verification enabled on your Google account. Here's how to generate it and use it securely in your script.

Step 1: Enable 2-Step Verification (If Not Already Enabled)
Go to your Google Account: https://myaccount.google.com.
In the left sidebar, select Security.
Under the "Signing in to Google" section, click 2-Step Verification.
Follow the instructions to set up 2-Step Verification.
Step 2: Generate an App Password
Go to your Google Account: https://myaccount.google.com.
In the left sidebar, select Security.
Scroll down to "App passwords" under the "Signing in to Google" section.
You may be asked to log in again.
Under "Select app", choose Mail.
Under "Select device", choose Other (Custom name) and enter a name like Python email script.
Click Generate.
You’ll see a 16-character password, like: eemxnlaqbrswxvaa. Copy this password.
Step 3: Use the App Password in Your Python Script
In your Python script, when prompted for your email password, use the App Password instead of your regular Gmail password.
For example:
python
Copy code
password = 'eemxnlaqbrswxvaa'  # Use the generated app password here
Never share your app password or hardcode it directly in shared scripts. Consider using environment variables or secure vaults to store it safely.
