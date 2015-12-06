*****Automation framework*****

1. Save code in Git
2. Install Jenkins on server
3. Install Pip
4. Install Python
5. Install Selenium
6. Install IE driver ( to run the tests on IE browser )
7. Install GChrome driver ( to run the tests on Chrome browser )



INSTALL AND SETUP GHROME_DRIVER:

 * The IEDriverServer exectuable must be downloaded ( http://www.seleniumhq.org/download/ ) and placed in your PATH.


INSTALL AND SETUP IE_DRIVER:

 * The IEDriverServer exectuable must be downloaded ( http://www.seleniumhq.org/download/ ) and placed in your PATH.
 * On IE 7 or higher on Windows Vista or Windows 7, you must set the Protected Mode settings for each zone to be the same value. The value can be on or off, as long as it is the same for every zone. To set the Protected Mode settings, choose "Internet Options..." from the Tools menu, and click on the Security tab. For each zone, there will be a check box at the bottom of the tab labeled "Enable Protected Mode".
 * Additionally, "Enhanced Protected Mode" must be disabled for IE 10 and higher. This option is found in the Advanced tab of the Internet Options dialog.
 * The browser zoom level must be set to 100% so that the native mouse events can be set to the correct coordinates.
 * For IE 11 only, you will need to set a registry entry on the target computer so that the driver can maintain a connection to the instance of Internet Explorer it creates. For 32-bit Windows installations, the key you must examine in the registry editor is HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_BFCACHE. For 64-bit Windows installations, the key is HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_BFCACHE. Please note that the FEATURE_BFCACHE subkey may or may not be present, and should be created if it is not present. Important: Inside this key, create a DWORD value named iexplore.exe with the value of 0.
