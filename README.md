# Simple_encryption_decryption_web_app
### steps:

- Step 1: Set Up Your Project in VSCode
Open VSCode:
Launch Visual Studio Code on your machine.
In VSCode, go to File > Open Folder and select the folder you just cloned.
Create a Virtual Environment:
Open the terminal in VSCode (View > Terminal) and run the following command to create a virtual environment:

python -m venv venv
This will create a venv/ folder inside your project directory.
Activate the Virtual Environment:
On Windows:
venv\Scripts\activate
On macOS/Linux:
source venv/bin/activate
Install Flask and Cryptography Libraries:

With the virtual environment activated, install the necessary packages:
pip install flask cryptography
- Step 2: 
Here’s how your folder structure should look:

* flask_crypto_server/ (main project folder)
* venv/ (virtual environment)
* keys/ (folder for storing keys)
private_key.pem
public_key.pem
app.py (main Flask app)
You can create the keys folder by right-clicking on your project folder in the VSCode file explorer and selecting "New Folder".

- Step 3: run  the server
  python app.py
- Step 4: Access the Frontend
Open your web browser and go to http://127.0.0.1:5000/.
You should see a simple web page with two forms: one for encrypting data and another for decrypting it.
- Step 5: Test Encryption
In the "Encrypt Data" form:

Enter some text into the "Data to Encrypt" input field (e.g., "Hello, World!").
Click the "Encrypt" button.
View the Encrypted Data:

The encrypted data will appear below the form under "Encrypted Data".
4. Test Decryption
In the "Decrypt Data" form:

Copy the encrypted data from the "Encrypted Data" field.
Paste it into the "Data to Decrypt" input field.
Click the "Decrypt" button.
View the Decrypted Data:

The decrypted data will appear below the form under "Decrypted Data".
5. Verify the Process
Check the Encryption: Ensure the encrypted data is a long string of hexadecimal characters, which is typical for encrypted outputs.
Check the Decryption: Verify that the decrypted data matches the original input data.
Example Workflow
Step a: Enter Hello, World! in the "Data to Encrypt" field.
Step b: Click "Encrypt" and note the encrypted output (something like 0a1b2c3d...).
Step c: Copy the encrypted data, paste it into the "Data to Decrypt" field, and click "Decrypt".
Step d: The decrypted data should display as Hello, World!.
