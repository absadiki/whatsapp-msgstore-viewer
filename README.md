# Whatsapp Msgstore Viewer
Free, open source and cross-platform app to decrypt, read and view the Whatsapp `msgstore.db` database.

<p align="center">
  <img src="./assets/demo/demo_gif_2.gif">
</p>

## Features
* View contact and group chats. 
* View call logs with their durations.
* Easy access to media files (images, audios and videos) from inside the chat, if the local Whatsapp directory has been provided. 
* Decrypt and view the database if you have the decryption `key` (Should support **crypt12**, **crypt14** and **crypt15**).
* Cross-platform (Should work on Linux, Windows and Mac)


## Installation
* ### Download pre-built binaries
  Pre-built binaries are available on the releases page. 
(Soon) 
* ### From source
  * Make sure you’re using Python 3.9
  * Create and activate a virtual environment.
  * Clone the repository
    ```bash 
    git clone https://github.com/absadiki/whatsapp-msgstore-viewer
    cd whatsapp-msgstore-viewer
    ```
  * Install the requirements
    ```bash 
    pip install -r requirements.txt
    ```
  * Run the main script
    ```bash 
    python main.py
    ```
> **Note:** Ubuntu users may run into some setup quirks. For guidance, see [#19](https://github.com/absadiki/whatsapp-msgstore-viewer/issues/19) 

## Usage
To use the app, you will need:
* The `msgstore.db` (`msgstore.db.cryptX` if it is encrypted) database: It is a database where Whatsapp is storing all your messages.
* The `wa.db` database: It is a database where Whatsapp is storing contact names. It is optional, so if it is not provided you will just see phone numbers.
* The `Whatsapp directory`: The directory of Whatsapp in the local storage of your phone. This will be used to view the media files (Optional as well).
* The `key`: If your database is encrypted, you will need to provide the decryption key to decrypt it first.  
  If your database is encrypted with <ins>crypt15/e2e</ins> (64‑digit encryption key), you can use `encrypted_backup.key` or convert your <ins>64‑digit key</ins> into a `.txt` file.  
  The decrypted database will be stored in the same directory of your encrypted database suffixed with `-decrypted.db`
  (See bellow for more information).

## Notes
* #### Where to find the databases
  Check the great tutorial "[Retrieving WhatsApp Databases](https://github.com/Dexter2389/whatsapp-backup-chat-viewer#retrieving-whatsapp-databases)" made by [@Dexter2389](https://github.com/Dexter2389).

* #### About the decryption process
  The app is using the [wa-crypt-tools](https://github.com/ElDavoo/wa-crypt-tools) by [ElDavoo](https://github.com/ElDavoo) under the hood.

  Please check their repository if you face any issues with the decryption. 

* #### About the Database schema
  Because this app is only a reverse engineering attempt of the Whatsapp database, it is very likely that it might break
in case there have been any updates to the `msgstore` database.

  For now it supports just the schema of my personal `msgstore.db` file.

  So I made it easy to allow the community to add support to more schemas (It's a simple SQLite exercise :D).

  All contributions are welcome. Feel free to let me know if you need any help.

  Follow these steps in order to add support to other schemas (see `db/v1/db.py` as an example):
  * Create a package in the `dbs` package and give your schema a name (for example `v2`).
  * Inside the newly created package, create a python module `db.py`.
  * Inherit the abstract class `AbstractDatabase` located in the `dbs/abstract_db.py` module.
  * The app will dynamically load existing schemas when starting. 
  * Submit a pull request. 

* #### About different languages

  - You might face an issue where the messages are being displayed in a wierd way (square characters).
  This is probably a font issue. To fix that, search for a font that supports your language, and on the login screen, go to
  `advanced settings` and provide the path to your font.
  - For RTL languages, please see [RTL Support #8](https://github.com/absadiki/whatsapp-msgstore-viewer/discussions/8)

## Contributing
If you find a bug, have a suggestion or feedback, please open an issue for discussion.

## Credits

- [kivy](https://kivy.org) & [KivyMD](https://kivymd.readthedocs.io) for the UI framework.
- [WhatsApp-Redesign](https://github.com/haddiebakrie/WhatsApp-Redesign) for the design inspiration and some UI components.
- [wa-crypt-tools](https://github.com/ElDavoo/wa-crypt-tools) for the decryption algorithm.
- [Sbk2605](https://commons.m.wikimedia.org/wiki/File:Whatsapp_logo.jpg) for the Whatsapp logo (Licenced under [Creative Commons Attribution-Share Alike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/deed.en)).
- [whatsapp-chat-parser-website](https://github.com/Pustur/whatsapp-chat-parser-website) for the background image.

And so many more libraries and frameworks.


## License

This project is licensed under the GNU General Licence version 3 or later. You can modify or redistribute it under the conditions
of these licences (See [LICENSE](./LICENSE) for more information).

## DISCLAIMER
This project is not endorsed or certified by WhatsApp Inc. and is meant for **personal and educational purposes only**.

It is provided as is without any express or implied warranties.

The authors/maintainers/contributors assume no responsibility for errors or omissions, or for damages resulting from the use of the information contained herein.
