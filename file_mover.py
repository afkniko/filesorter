import shutil
import os
class Filemover:

    def __init__(self):

        # List of extensions
        self.extensions = {
            "audio": [
                ".aif", # AIF Audio file
                ".cda", # CD audio track
                ".mid", # MIDI Audio
                ".mp3", # MP3 Audio
                ".mpa", # MPEG-2 audio
                ".ogg", # Ogg Vorbis audio
                ".wav", # WAV file
                ".wma", # WMA Audio
                ".wpl" # Windows Media Player playlist
                ],

            "compressed" : [
                ".7z", # 7-zip compressed
                ".arj", # ARJ compressed
                ".deb", # Debian software package
                ".pkg", # Package file
                ".rar", # RAR file
                ".rpm", # Red Hat Package Manager
                ".tar.gz", # Tarball compressed
                ".z", # Z compressed
                ".zip" # Zip compressed
                ],

            "disc" : [
                ".bin", # Binary disc
                ".dmg", # macOS X disk img
                ".iso", # ISO DISC
                ".ISO", # ISO DISC
                ".toast", # Toats disc img
                ".vcd" # Virtual CD
                ],

            "data" : [
                ".csv", # Comma separated value file
                ".dat", # Data file
                ".db", # Database file
                ".dbf", # Database file
                ".log", # Log file
                ".mdb", # Microsoft Access database file
                ".sav", # Save file
                ".sql", # SQL Database file
                ".tar", # Linux tarball file archive
                ".xml" # XML file
                ],

            "email" : [
                ".email", # Outlook Express e-mail message
                ".eml", # E-mail message file from multiple e-mail clients, including Gmail.
                ".emlx", # Apple Mail e-mail
                ".msg", # Microsoft Outlook e-mail message file.
                ".oft", # Microsoft Outlook e-mail template file.
                ".ost", # Microsoft Outlook offline e-mail storage file.
                ".pst", # Microsoft Outlook e-mail storage file.
                ".vcf" # E-mail contact file.
                ],

            "executable" : [
                ".apk", # Android package file
                ".bat", # Batch file
                ".bin", # Binary file
                ".com", # MS-DOS command file
                ".exe", # Executable file
                ".gadget", # Windows gadget
                ".jar", # Java Archive file
                ".msi", # Windows installer package
                ".wsf" # Windows Script File
                ],


            "font" : [
                ".fnt", #- Windows font file
                ".fon", # - Generic font file
                ".otf", # - Open type font file
                ".ttf", # - TrueType font file
                ],

            "image" : [
                ".ai", # - Adobe Illustrator file
                ".bmp", # - Bitmap image
                ".gif", # - GIF image
                ".ico", # - Icon file
                ".jpeg", # - JPEG image
                ".jpg", # - JPEG image
                ".png", #- PNG image
                ".ps", # - PostScript file
                ".psd", # - PSD image
                ".svg", # - Scalable Vector Graphics file
                ".tif", # - TIFF image
                ".tiff", # - TIFF image
                ],

            "internet" : [
                ".asp",  #- Active Server Page file
                ".aspx", #- Active Server Page file
                ".cer", #- Internet security certificate
                ".cfm", #- ColdFusion Markup file
                ".css", #- Cascading Style Sheet file
                ".htm", #- HTML file
                ".html", #- HTML file
                ".js", #- JavaScript file
                ".jsp", #- Java Server Page file
                ".part", #- Partially downloaded file
                ".rss", #- RSS file
                ".xhtml" #- XHTML file
                ],

            "presentation" : [
                ".key", #- Keynote presentation
                ".odp", #- OpenOffice Impress presentation file
                ".pps", #- PowerPoint slide show
                ".ppt", #- PowerPoint presentation
                ".pptx", #- PowerPoint Open XML presentation
                ],

            "programming" : [
                ".c", #- C and C++ source code file
                ".cgi", # Perl
                ".pl", #- Perl script file.
                ".class" #- Java class file
                ".cpp" #- C++ source code file
                ".cs" #- Visual C# source code file
                ".h" #- C, C++, and Objective-C header file
                ".java", #- Java Source code file
                ".php", #- PHP script file.
                ".py", #- Python script file.
                ".sh", #- Bash shell script
                ".swift", #- Swift source code file
                ".vb" #- Visual Basic file
                ],

            "spreadsheet" : [
                ".ods", # OpenOffice Calc spreadsheet file
                ".xls", # Microsoft Excel file
                ".xlsm", # Microsoft Excel file with macros
                ".xlsx" # Microsoft Excel Open XML spreadsheet file
                ],

            "video" : [
                ".3g2", # 3GPP2 multimedia file
                ".3gp", # 3GPP multimedia file
                ".avi", # AVI file
                ".flv", # Adobe Flash file
                ".h264", # H.264 video file
                ".m4v", # Apple MP4 video file
                ".mkv", # Matroska Multimedia Container
                ".mov", # Apple QuickTime movie file
                ".mp4", # Apple QuickTime movie file
                ".mpg", # MPEG video file
                ".mpeg", # MPEG video file
                ".rm", # RealMedia file
                ".swf", # Shockwave flash file
                ".vob", # DVD Video Object
                ".wmv" # Windows Media Video file
                ],

            "text" : [
                ".doc", # Microsoft Word file
                ".docx", # Microsoft Word file
                ".odt", # OpenOffice Writer document file
                ".pdf", # PDF file
                ".rtf", # Rich Text Format
                ".tex", # A LaTeX document file
                ".txt", # Plain text file
                ".wpd", # WordPerfect document
                ".md"
                ]
        }

        # Set directory where to sort files
    def scan_files(self, directory, checked_items):
        
        self.parent_dir = directory
        self.checked_items = checked_items
        self.count = 0
        # Items in directory
        self.dir_items = os.listdir(self.parent_dir)
        try:
        # Scan extensions keys and values          
            for item in self.checked_items:
                for key, value in self.extensions.items():
                    # Check which extensions to look for
                    if key == item:

                    # Scan files in directory
                        for dir_item in self.dir_items:
                            # Compare directory file extension to each value in dictionary
                            for v in value:
                                if dir_item.endswith(v): 
                                    
                                    # Generate source path and destination path
                                    source = os.path.join(self.parent_dir, dir_item).replace("/","\\")
                                    destination = os.path.join(self.parent_dir, key).replace("/","\\")
                                    
                                    # If extension folder doesn't exist, create folder and move file to it
                                    if not os.path.exists(destination):
                                        os.makedirs(destination)
                                        shutil.move(source , destination)
                                        self.count += 1
                                    else:
                                        # If extension folder exists and move file to it
                                        shutil.move(source , destination)
                                        self.count += 1
            # Send count of sorted items     
            return self.count                    
            
        except FileNotFoundError as err:
            return type(err)      
        
        
