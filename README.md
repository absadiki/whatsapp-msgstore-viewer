# whatsapp Msgstore Viewer
Free, open source and cross-platform app to decrypt, read and view the Whatsapp `msgstore.db` database.
<br/>
<p align="center">
  <img src="./assets/demo/demo_gif_2.gif">
</p>

# Features
* View contact and group chats.
* View call logs with their durations.
* Easy access to media files (images, audio, and video) from within the chat, if the local WhatsApp directory has been provided.
* Decrypt and view the database if you have the decryption `key` (Should support **crypt12**, **crypt14**, and **crypt15**).
* Cross-platform (Should work on Linux, Windows, and Mac)


# Installation

### Prerequisites
- Python 3.9 or later

### Quick Install (Recommended)
```bash
pip install git+https://github.com/absadiki/whatsapp-msgstore-viewer.git
```

### Running the Application
After installation, start the application with:
```bash
wmv
```

### Development Setup
For contributing or modifying the source:
```bash
git clone https://github.com/absadiki/whatsapp-msgstore-viewer
cd whatsapp-msgstore-viewer
pip install -e .
```

> **Note for Ubuntu users:** Additional system dependencies might be needed. See [#19](https://github.com/absadiki/whatsapp-msgstore-viewer/issues/19) for details.

# Usage
To use the app, you will need:
* The `msgstore.db` (`msgstore.db.cryptX` if it is encrypted) database: It is a database where Whatsapp is storing all your messages.
* The `wa.db` database: It is a database where Whatsapp is storing contact names. It is optional, so if it is not provided you will just see phone numbers.
* The `WhatsApp directory`: The directory of WhatsApp in the local storage of your phone. This will be used to view the media files (Optional as well).
* The `key`: If your database is encrypted, you will need to provide the decryption key to decrypt it. The decrypted database will be stored in the same directory as your encrypted database with a `-decrypted.db` suffix.
  (See below for more information).

# Notes
#### Where to find the databases
Check out the great tutorial "[Retrieving WhatsApp Databases](https://github.com/Dexter2389/whatsapp-backup-chat-viewer#retrieving-whatsapp-databases)" by [@Dexter2389](https://github.com/Dexter2389).

#### About the decryption process
The app uses the [WhatsApp-Crypt14-Crypt15-Decrypter](https://github.com/ElDavoo/WhatsApp-Crypt14-Crypt15-Decrypter) by [ElDavoo](https://github.com/ElDavoo) under the hood.
Please check their repository if you face any issues with the decryption.

#### About the Database schema
This app is a reverse engineering attempt of the WhatsApp database and has been tested with my personal `msgstore.db` file. It might break if there are any updates to the `msgstore` database schema.

I've made it easy to add support for more schemas (It's a simple SQLite exercise :D).

All contributions are welcome.

Follow these steps to add support for other schemas (see `db/v1/db.py` as an example):
* Create a package in the `dbs` package and give your schema a name (for example `v2`).
* Inside the newly created package, create a Python module `db.py`.
* Inherit the abstract class `AbstractDatabase` located in the `dbs/abstract_db.py` module.
* The app will dynamically load existing schemas when starting.
* Submit a pull request.

#### About different languages

  - You might encounter an issue where messages are displayed incorrectly (as square characters).
  This is likely a font issue. To resolve this, find a font that supports your language and specify its path in the `advanced settings` on the login screen.
  - For RTL languages, please see [RTL Support #8](https://github.com/absadiki/whatsapp-msgstore-viewer/discussions/8)

# Contributing
If you find a bug, have a suggestion or feedback, please open an issue for discussion.


# License

This project is licensed under the GNU General Public License version 3 or later. You can modify or redistribute it under the conditions
of these licenses (See [LICENSE](./LICENSE) for more information).

# DISCLAIMER
This project is not endorsed or certified by WhatsApp Inc. and is meant for **personal and educational purposes only**.

It is provided 'as is' without any express or implied warranties.

The authors, maintainers, and contributors assume no responsibility for errors, omissions, or damages resulting from the use of this information.
