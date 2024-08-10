import subprocess

Contents="""
------------------------------------------------------------------

Game Clients:
------------------------------------------------------------------
1. Steam
2. Epic Games
3. Riot client [Currently unavailable]
4. Ubisoft connect
_________________________________________________________________

Driver Updaters:
-----------------------------------------------------------------
5. Driver booster
6. Geforce Experience (NVIDIA)
7. AMD Adrenaline
8. Intel Driver and support assistant
9. NVIDIA App (beta)
_________________________________________________________________

OEM Software:
-----------------------------------------------------------------
10. Armoury Crate (Asus)
11. MSI Center 
12. Corsair iCUE
13. Logitech G HUB
14. Alienware Command Center
15. Razer Synapse
16. Gigabyte AORUS Engine
________________________________________________________________

RGB Control:
----------------------------------------------------------------
17. SignalRGB
18. ASUS Aura Sync (now an aurmoury crate feature) [10]
19. MSI Mystic Light (Now an MSI center feature) [11]
20. Gigabyte RGB Fusion
21. Thermaltake RGB Plus
22. HYTE Nexus
23. NZXT CAM
_________________________________________________________________

Tools:
-----------------------------------------------------------------
24. Rufus
25. Revo Uninstaller
26. 7Zip
27. Power Toys [Currently unavailable]
________________________________________________________________

Network "Tools":
----------------------------------------------------------------
28. Angry IP Scanner
29. Nmap/Zenmap
30. SoftPerfect network scanner
_______________________________________________________________

Benchmarking software:
---------------------------------------------------------------
31. Performance Test
32. User Benchmark
33. Cinebench R24 [Currently unavailable]
34. CrystalDiskMark
_______________________________________________________________

System info and tweaking:
---------------------------------------------------------------
35. CPU-Z
36. GPU Tweak III (Asus)
37. MSI Afterburner
______________________________________________________________

Other software:
---------------------------------------------------------------
38. CapCut
39. VMware Player
40. Python
41. Visual Studio Code
______________________________________________________________



"""

def install_package(exe_path):
    subprocess.run(exe_path)

Entry_door=input("Press 'Enter' to begin...")

print(Contents)

Item_selector=input("Enter the number that corresponds to the software that you wish to install: ")

if Item_selector=="1":
    file_name="SteamSetup"
elif Item_selector=="2":
    file_name="EpicInstaller-15.17.1-9d82633a29aa4914a16ae4b7a65e68bd"
elif Item_selector=="3":
    file_name="Not Avalible"
elif Item_selector=="4":
    file_name="UbisoftConnectInstaller"
elif Item_selector=="5":
    file_name="driver_booster_setup"
elif Item_selector=="6":
    file_name="GeForce_Experience_v3.28.0.417"
elif Item_selector=="7":
    file_name="amd-software-adrenalin-edition-24.7.1-minimalsetup-240805_web"
elif Item_selector=="8":
    file_name="Intel-Driver-and-Support-Assistant-Installer"
elif Item_selector=="9":
    file_name="NVIDIA_app_beta_v10.0.2.207"
elif Item_selector=="10":
    file_name="ArmouryCrateInstaller"
elif Item_selector=="11":
    file_name="MSI Center_2.0.39.0"
elif Item_selector=="12":
    file_name="Install iCUE"
elif Item_selector=="13":
    file_name="lghub_installer"
elif Item_selector=="14":
    file_name="Alienware-Command-Center-Application-Full-Installer_7NNR0_WIN_5.5.26.0_A00_02"
elif Item_selector=="15":
    file_name="RazerSynapseInstaller_V1.19.0.635"
elif Item_selector=="16":
    file_name="AORUS_ENGINE_SETUP_V2.2.8_B240718_x86_Signed"
elif Item_selector=="17":
    file_name="Install_SignalRgb"
elif Item_selector=="18":
    file_name="ArmouryCrateInstaller"
elif Item_selector=="19":
    file_name="MSI Center_2.0.39.0"
elif Item_selector=="20":
    file_name="GIGABYTE Control Center_2024_Jun_release_All_Setup_B240702"
elif Item_selector=="21":
    file_name="TT RGB PLUS_Setup_2.1.5_x64"
elif Item_selector=="22":
    file_name="HYTE Nexus Setup 1.5.520"
elif Item_selector=="23":
    file_name="NZXT-CAM-Setup"
elif Item_selector=="24":
    file_name="rufus-4.5p"
elif Item_selector=="25":
    file_name="revosetup"
elif Item_selector=="26":
    file_name="7z2407-x64"
elif Item_selector=="27":
    file_name="Not Avalible"
elif Item_selector=="28":
    file_name="ipscan-3.9.1-setup"
elif Item_selector=="29":
    file_name="nmap-7.95-setup"
elif Item_selector=="30":
    file_name="netscan_setup"
elif Item_selector=="31":
    file_name="petst"
elif Item_selector=="32":
    file_name="UserBenchmarkInstaller"
elif Item_selector=="33":
    file_name="Not Avalible"
elif Item_selector=="34":
    file_name="CrystalDiskMark8_0_5"
elif Item_selector=="35":
    file_name="cpu-z_2.10-en"
elif Item_selector=="36":
    file_name="GPU Tweak III Install"
elif Item_selector=="37":
    file_name="MSIAfterburnerSetup465"
elif Item_selector=="38":
    file_name="CapCut_7367248652886130705_installer"
elif Item_selector=="39":
    file_name="VMware-player-17.5.2-23775571"
elif Item_selector=="40":
    file_name="python-3.12.5-amd64"
elif Item_selector=="41":
    file_name="VSCodeUserSetup-x64-1.92.1"
else:
    print("Invalid entry. Closing...")
    exit()

if file_name=="EpicInstaller-15.17.1-9d82633a29aa4914a16ae4b7a65e68bd":
    final_path="C:\\Installers\\EpicInstaller-15.17.1-9d82633a29aa4914a16ae4b7a65e68bd.msi"
elif (file_name=="Not Avalible"):
    print("""
    This item is not yet avalible. Closing...
          

    """)
    exit()
else:
    final_path=f"C:\\Installers\\{file_name}.exe"

# print(final_path)

install_door=input(f"""
Press 'Enter' to proceed with installing software #{Item_selector}... 

""")

print("Launching installer...")

install_package(final_path)

print("Closing Wraith Installer")