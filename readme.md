
# ☯️ WR4TH



WR4TH is a network-based remote access trojan designed for Linux environments that enables users to bypass Windows Defender. This tool allows seamless SSH access to Windows devices on the same network, providing advanced remote control capabilities.


## ⚠️ Disclaimer:

WR4TH is intended for educational and research purposes only. The use of this tool on systems without explicit permission is illegal and unethical. By using this software, you acknowledge that you are responsible for your actions and comply with all applicable laws and regulations. The developers of WR4TH are not liable for any misuse or damages resulting from the use of this tool. Always obtain proper authorization before testing the security of any network or device.

## 📸 Screenshot:

![App Screenshot](https://i.ibb.co/2K8hBGD/de819c7f-88ba-4f58-9558-dc8cb4d6d057.png)


## 🎥 Demo:

[![YouTube](http://i.ytimg.com/vi/2BFzcmkbUMM/hqdefault.jpg)](https://www.youtube.com/watch?v=2BFzcmkbUMM)

## ✅ Features:

- Bypasses Windows Defender **[Tested on 4/10/2024]**
- Full Control Over Targeted Device via SSH
- Upload and Execute File
- Download File
- Easy to use via Terminal
- Persistent Connection
## ⚙️ Pre-Requisites:

1. Install sshpass

   ```apt install sshpass```

2. signup for [mail-trap](https://mailtrap.io/)

3. In email-testing, copy **Username** and **Password**.

4. Replace the **USERNAME** and **PASSWORD** in system.ps1 [in client folder] in 
line 67.

5. Upload the ps1 file on github and copy the raw link.

6. Replace the **raw url** in **java.bat** in **line 48**

7. Replace the **raw url** in **initial.bat** in **line 6**

8.  Done






## 💡 Usage:

1. After the file is executed, after a while you will recieve an email in your smtp inbox

2. Download the attachment, in the main wr4th folder

3. Install colorama

```pip install colorama```

4. Open terminal in the same directory and run the command

```python main.py filename.rat```
## ❓ FAQ

#### 1. **What is WR4TH?**
WR4TH is a network-based remote access trojan designed for Linux that enables users to bypass Windows Defender and gain SSH access to Windows devices on the same network.

#### 2. **Is WR4TH legal to use?**
WR4TH is intended for educational and research purposes only. Using it on systems without explicit permission is illegal and unethical. Always ensure you have authorization before testing any network or device.

#### 3. **What environments does WR4TH support?**
WR4TH is built to run on Linux and is specifically designed to exploit Windows devices on the same local network.

#### 4. **Do I need special permissions to use WR4TH?**
Yes, you must have explicit permission from the owner of the network and devices you are testing. Unauthorized access to systems is illegal.

#### 5. **Can WR4TH be detected by antivirus software?**
WR4TH is designed to bypass Windows Defender; however, no tool can guarantee complete invisibility. The effectiveness of detection can vary based on the security configurations of the target system.
## 🪪 License

[MIT](https://choosealicense.com/licenses/mit/)


## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/adithya-poojary-1771b9331)

