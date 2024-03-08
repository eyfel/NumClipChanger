# NumClipChanger
That dynamically updates a GUI with clipboard content, and allows users to increment or decrement numerical values at the end of the text. Ideal for managing serial codes or numbers quickly.



**NumClipChanger** offers a unique blend of clipboard management and GUI interaction, enabling users to:

- **Display Real-Time Clipboard Content**: Immediately shows the current text copied to the clipboard in a dynamically updated GUI window, ensuring users always know what's in their clipboard.
- **Automatically Increment and Decrement Values**: With simple keyboard shortcuts, users can modify numerical values found at the end of the clipboard text, facilitating tasks that involve sequential numbering or code adjustments.
- **Customizable User Interface**: Features a high-contrast, easy-to-read display that can be kept on top of other windows, making it a convenient tool for multitasking and workflow optimization.
- **Effortless Integration and Use**: Designed to run quietly in the background, PanelArt activates with specific keyboard shortcuts, blending seamlessly into the user's workflow without intrusive pop-ups or complex configurations.
- **Cross-Platform Compatibility**: Built with Python, it leverages widely supported libraries, making it adaptable to various operating systems with minimal adjustments.
- **Open Source for Customization**: Users with programming knowledge can easily modify or extend the script's functionalities, thanks to its open-source nature, accommodating specific use cases or preferences.

  ### How to Use NumClipChanger

NumClipChanger is designed to be straightforward and user-friendly, focusing on enhancing your productivity with clipboard content. Here's how to get started:

1. **Install Required Libraries**: Ensure you have a `requirements.txt` file with the following libraries listed:
   ```
   pyperclip
   keyboard
   ```
   Install these dependencies by running `pip install -r requirements.txt` in your terminal.

2. **Start the Script**: Run the NumClipChanger script. Once started, it will display the current content of your clipboard in a GUI window.

3. **Using Keyboard Shortcuts**:
   - Press the `e` key to increment the last numerical value found in your clipboard content. For example, if your clipboard contains "Code-123", pressing `e` will change it to "Code-124".
   - Press the `r` key to decrement the last numerical value. Using the previous example, "Code-123" would change to "Code-122".

The GUI window updates in real-time to reflect changes, showing the modified clipboard content. NumClipChanger works silently in the background, allowing you to continue with your tasks without interruption.
