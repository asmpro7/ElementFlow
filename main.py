# -*- coding: utf-8 -*-

import sys,os
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

from flowlauncher import FlowLauncher, FlowLauncherAPI
import json
import subprocess
import os
from PIL import Image

def image(color_hex):
    color = tuple(int(color_hex[i:i+2], 16) for i in (0, 2, 4))
    width, height = 200, 200
    file_name = f"{color_hex}.png"
    dir_name = "colors"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    file_path = os.path.join(dir_name, file_name)
    image = Image.new('RGB', (width, height), color)
    image.save(file_path, "PNG")

def copy2clip(txt):
    txt=str(txt)
    cmd = 'echo '+txt+'|clip'
    return subprocess.check_call(cmd, shell=True)
with open("elements.json","r") as e:
    elements=json.load(e)

class ElementFlow(FlowLauncher):

    def query(self, query):
        results=[]
        try:
              
            if len(query.strip()) == 0:
                        results.append({
                            "Title": "Enter the element you want",
                            "SubTitle": "you can use element name, atomic number and symbol",
                            "IcoPath": "Images/app.png"})
                        results.append({
                            "Title": "Enter the Data you want",
                            "SubTitle": "you can use names, groups and numbers",
                            "IcoPath": "Images/app.png"})

            elif query.isdigit():
                query=int(query)
                if [element["cpkHexColor"] for element in elements if element["atomicNumber"]==query][0] == "unknown":
                     ImgCol="Images/un.png"
                else:
                     color_hex=[element["cpkHexColor"] for element in elements if element["atomicNumber"]==query][0]
                     image(color_hex)
                     ImgCol=f"colors/{color_hex}.png"
                
                EleNam_AtoNum=[element["name"] for element in elements if element["atomicNumber"]==query][0]
                results.append({
                            "Title": f"Name: {EleNam_AtoNum}",
                            "IcoPath": "Images/app.png",
                            "JsonRPCAction": {"method": "copy", "parameters": [EleNam_AtoNum] }
                            })
                EleSym_AtoNum=[element["symbol"] for element in elements if element["atomicNumber"]==query][0]
                results.append({
                            "Title": f"Symbol: {EleSym_AtoNum}",
                            "IcoPath": "Images/app.png",
                            "JsonRPCAction": {"method": "copy", "parameters": [EleSym_AtoNum] }
                            })
                EleNum_AtoNum=[element["atomicNumber"] for element in elements if element["atomicNumber"]==query][0]
                results.append({
                            "Title": f"Atomic Number: {EleNum_AtoNum}",
                            "IcoPath": "Images/app.png",
                            "JsonRPCAction": {"method": "copy", "parameters": [EleNum_AtoNum] }
                            })
                EleMas_AtoNum=[element["atomicMass"] for element in elements if element["atomicNumber"]==query][0]
                results.append({
                            "Title": f"Atomic Mass: {EleMas_AtoNum}",
                            "IcoPath": "Images/app.png",
                            "JsonRPCAction": {"method": "copy", "parameters": [EleMas_AtoNum] }
                            })
                ElePer_AtoNum=[element["period"] for element in elements if element["atomicNumber"]==query][0]
                results.append({
                            "Title": f"Period: {ElePer_AtoNum}",
                            "IcoPath": "Images/app.png",
                            "JsonRPCAction": {"method": "copy", "parameters": [ElePer_AtoNum] }
                            })
                EleGer_AtoNum=[element["group"] for element in elements if element["atomicNumber"]==query][0]
                results.append({
                            "Title": f"Group: {EleGer_AtoNum}",
                            "IcoPath": "Images/app.png",
                            "JsonRPCAction": {"method": "copy", "parameters": [EleGer_AtoNum] }
                            })
                EleBlo_AtoNum=[element["block"] for element in elements if element["atomicNumber"]==query][0]
                results.append({
                            "Title": f"Block: {EleBlo_AtoNum}",
                            "IcoPath": "Images/app.png",
                            "JsonRPCAction": {"method": "copy", "parameters": [EleBlo_AtoNum] }
                            })
                EleCon_AtoNum=[element["electronicConfiguration"] for element in elements if element["atomicNumber"]==query][0]
                results.append({
                            "Title": f"Electronic Configuration: {EleCon_AtoNum}",
                            "IcoPath": "Images/app.png",
                            "JsonRPCAction": {"method": "copy", "parameters": [EleCon_AtoNum] }
                            })
                EleOxi_AtoNum=[element["oxidationStates"] for element in elements if element["atomicNumber"]==query][0]
                results.append({
                            "Title": f"Oxidation States: {EleOxi_AtoNum}",
                            "IcoPath": "Images/app.png",
                            "JsonRPCAction": {"method": "copy", "parameters": [EleOxi_AtoNum] }
                            })
                EleGrb_AtoNum=[element["groupBlock"] for element in elements if element["atomicNumber"]==query][0]
                results.append({
                            "Title": f"Group Block: {EleGrb_AtoNum}",
                            "IcoPath": "Images/app.png",
                            "JsonRPCAction": {"method": "copy", "parameters": [EleGrb_AtoNum] }
                            })
                EleSts_AtoNum=[element["standardState"] for element in elements if element["atomicNumber"]==query][0]
                results.append({
                            "Title": f"Standard State: {EleSts_AtoNum}",
                            "IcoPath": "Images/app.png",
                            "JsonRPCAction": {"method": "copy", "parameters": [EleSts_AtoNum] }
                            })
                EleEcg_AtoNum=[element["electronegativity"] for element in elements if element["atomicNumber"]==query][0]
                results.append({
                            "Title": f"Electronegativity: {EleEcg_AtoNum}",
                            "IcoPath": "Images/app.png",
                            "JsonRPCAction": {"method": "copy", "parameters": [EleNam_AtoNum] }
                            })
                EleAtr_AtoNum=[element["atomicRadius"] for element in elements if element["atomicNumber"]==query][0]
                results.append({
                            "Title": f"Atomic Radius: {EleAtr_AtoNum}",
                            "IcoPath": "Images/app.png",
                            "JsonRPCAction": {"method": "copy", "parameters": [EleAtr_AtoNum] }
                            })
                EleIoR_AtoNum=[element["ionRadius"] for element in elements if element["atomicNumber"]==query][0]
                results.append({
                            "Title": f"Ion Radius: {EleIoR_AtoNum}",
                            "IcoPath": "Images/app.png",
                            "JsonRPCAction": {"method": "copy", "parameters": [EleIoR_AtoNum] }
                            })
                EleVDR_AtoNum=[element["vanDerWaalsRadius"] for element in elements if element["atomicNumber"]==query][0]
                results.append({
                            "Title": f"Van Der Waals Radius: {EleVDR_AtoNum}",
                            "IcoPath": "Images/app.png",
                            "JsonRPCAction": {"method": "copy", "parameters": [EleVDR_AtoNum] }
                            })
                EleIEn_AtoNum=[element["ionizationEnergy"] for element in elements if element["atomicNumber"]==query][0]
                results.append({
                            "Title": f"Ionization Energy: {EleIEn_AtoNum}",
                            "IcoPath": "Images/app.png",
                            "JsonRPCAction": {"method": "copy", "parameters": [EleIEn_AtoNum] }
                            })
                EleEAf_AtoNum=[element["electronAffinity"] for element in elements if element["atomicNumber"]==query][0]
                results.append({
                            "Title": f"Electron Affinity: {EleEAf_AtoNum}",
                            "IcoPath": "Images/app.png",
                            "JsonRPCAction": {"method": "copy", "parameters": [EleEAf_AtoNum] }
                            })
                EleBot_AtoNum=[element["bondingType"] for element in elements if element["atomicNumber"]==query][0]
                results.append({
                            "Title": f"Bonding Type: {EleBot_AtoNum}",
                            "IcoPath": "Images/app.png",
                            "JsonRPCAction": {"method": "copy", "parameters": [EleBot_AtoNum] }
                            })
                EleMep_AtoNum=[element["meltingPoint"] for element in elements if element["atomicNumber"]==query][0]
                results.append({
                            "Title": f"Melting Point: {EleMep_AtoNum}",
                            "IcoPath": "Images/app.png",
                            "JsonRPCAction": {"method": "copy", "parameters": [EleMep_AtoNum] }
                            })
                EleBop_AtoNum=[element["boilingPoint"] for element in elements if element["atomicNumber"]==query][0]
                results.append({
                            "Title": f"Boiling Point: {EleBop_AtoNum}",
                            "IcoPath": "Images/app.png",
                            "JsonRPCAction": {"method": "copy", "parameters": [EleBop_AtoNum] }
                            })
                EleDen_AtoNum=[element["density"] for element in elements if element["atomicNumber"]==query][0]
                results.append({
                            "Title": f"Density: {EleDen_AtoNum}",
                            "IcoPath": "Images/app.png",
                            "JsonRPCAction": {"method": "copy", "parameters": [EleDen_AtoNum] }
                            })
                EleDis_AtoNum=[element["yearDiscovered"] for element in elements if element["atomicNumber"]==query][0]
                results.append({
                            "Title": f"Year Discovered: {EleDis_AtoNum}",
                            "IcoPath": "Images/app.png",
                            "JsonRPCAction": {"method": "copy", "parameters": [EleDis_AtoNum] }
                            })
                
                EleCol_AtoNum=[element["cpkHexColor"] for element in elements if element["atomicNumber"]==query][0]
                results.append({
                            "Title": f"Color: {EleCol_AtoNum}",
                            "IcoPath": ImgCol,
                            "JsonRPCAction": {"method": "copy", "parameters": [EleCol_AtoNum] }
                            })




            
            elif query == "names":
                for eleNa in [element["name"] for element in elements]:
                    results.append({
                         "Title":f"{eleNa}",
                         "IcoPath":"Images/app.png",
                         "JsonRPCAction":{"method":"Flow.Launcher.ChangeQuery", "parameters":[f"ce {eleNa}",True] }
                    })   
            elif query == "numbers":
                for eleNa in [element["atomicNumber"] for element in elements]:
                    results.append({
                         "Title":f"{eleNa}",
                         "IcoPath":"Images/app.png",
                         "JsonRPCAction":{"method":"Flow.Launcher.ChangeQuery", "parameters":[f"ce {eleNa}",True] }
                    })   
            elif query == "groups":
                    results.append({
                         "Title":'alkaline earth metal',
                         "IcoPath":"Images/app.png",
                         "JsonRPCAction":{"method":"Flow.Launcher.ChangeQuery", "parameters":["ce alkaline earth metal",True] }
                    })   
                    results.append({
                         "Title":'lanthanoid',
                         "IcoPath":"Images/app.png",
                         "JsonRPCAction":{"method":"Flow.Launcher.ChangeQuery", "parameters":["ce lanthanoid",True] }
                    })   
                    results.append({
                         "Title":'metalloid',
                         "IcoPath":"Images/app.png",
                         "JsonRPCAction":{"method":"Flow.Launcher.ChangeQuery", "parameters":["ce metalloid",True] }
                    })   
                    results.append({
                         "Title":'post-transition metal',
                         "IcoPath":"Images/app.png",
                         "JsonRPCAction":{"method":"Flow.Launcher.ChangeQuery", "parameters":["ce post-transition metal",True] }
                    })   
                    results.append({
                         "Title":'noble gas',
                         "IcoPath":"Images/app.png",
                         "JsonRPCAction":{"method":"Flow.Launcher.ChangeQuery", "parameters":["ce noble gas",True] }
                    })   
                    results.append({
                         "Title":'alkali metal',
                         "IcoPath":"Images/app.png",
                         "JsonRPCAction":{"method":"Flow.Launcher.ChangeQuery", "parameters":["ce alkali metal",True] }
                    })   
                    results.append({
                         "Title":'halogen',
                         "IcoPath":"Images/app.png",
                         "JsonRPCAction":{"method":"Flow.Launcher.ChangeQuery", "parameters":["ce halogen",True] }
                    })   
                    results.append({
                         "Title":'actinoid',
                         "IcoPath":"Images/app.png",
                         "JsonRPCAction":{"method":"Flow.Launcher.ChangeQuery", "parameters":["ce actinoid",True] }
                    })   
                    results.append({
                         "Title":'metal',
                         "IcoPath":"Images/app.png",
                         "JsonRPCAction":{"method":"Flow.Launcher.ChangeQuery", "parameters":["ce metal",True] }
                    })   
                    results.append({
                         "Title":'transition metal',
                         "IcoPath":"Images/app.png",
                         "JsonRPCAction":{"method":"Flow.Launcher.ChangeQuery", "parameters":["ce transition metal",True] }
                    })   
                    results.append({
                         "Title":'nonmetal',
                         "IcoPath":"Images/app.png",
                         "JsonRPCAction":{"method":"Flow.Launcher.ChangeQuery", "parameters":["ce nonmetal",True] }
                    })   


            elif query in ['alkaline earth metal', 'lanthanoid', 'metalloid', 'post-transition metal', 'noble gas', 'alkali metal', 'halogen', 'actinoid', 'metal', 'transition metal', 'nonmetal']:
                for ex in [element["name"] for element in elements if element["groupBlock"]==query]:
                    results.append({
                         "Title":f"{ex}",
                         "IcoPath":"Images/app.png",
                         "JsonRPCAction":{"method":"Flow.Launcher.ChangeQuery", "parameters":[f"ce {ex}",True] }
                    })   





            elif query.isalpha and len(query) in [1,2]:
                        if [element["cpkHexColor"] for element in elements if element["symbol"]==query][0] == "unknown":
                            ImgCol="Images/un.png"
                        else:
                            color_hex=[element["cpkHexColor"] for element in elements if element["symbol"]==query][0]
                            image(color_hex)
                            ImgCol=f"colors/{color_hex}.png"
    
                        EleNam_AtoNum=[element["name"] for element in elements if element["symbol"]==query][0]
                        results.append({
                                    "Title": f"Name: {EleNam_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleNam_AtoNum] }
                                    })
                        EleSym_AtoNum=[element["symbol"] for element in elements if element["symbol"]==query][0]
                        results.append({
                                    "Title": f"Symbol: {EleSym_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleSym_AtoNum] }
                                    })
                        EleNum_AtoNum=[element["atomicNumber"] for element in elements if element["symbol"]==query][0]
                        results.append({
                                    "Title": f"Atomic Number: {EleNum_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleNum_AtoNum] }
                                    })
                        EleMas_AtoNum=[element["atomicMass"] for element in elements if element["symbol"]==query][0]
                        results.append({
                                    "Title": f"Atomic Mass: {EleMas_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleMas_AtoNum] }
                                    })
                        ElePer_AtoNum=[element["period"] for element in elements if element["symbol"]==query][0]
                        results.append({
                                    "Title": f"Period: {ElePer_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [ElePer_AtoNum] }
                                    })
                        EleGer_AtoNum=[element["group"] for element in elements if element["symbol"]==query][0]
                        results.append({
                                    "Title": f"Group: {EleGer_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleGer_AtoNum] }
                                    })
                        EleBlo_AtoNum=[element["block"] for element in elements if element["symbol"]==query][0]
                        results.append({
                                    "Title": f"Block: {EleBlo_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleBlo_AtoNum] }
                                    })
                        EleCon_AtoNum=[element["electronicConfiguration"] for element in elements if element["symbol"]==query][0]
                        results.append({
                                    "Title": f"Electronic Configuration: {EleCon_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleCon_AtoNum] }
                                    })
                        EleOxi_AtoNum=[element["oxidationStates"] for element in elements if element["symbol"]==query][0]
                        results.append({
                                    "Title": f"Oxidation States: {EleOxi_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleOxi_AtoNum] }
                                    })
                        EleGrb_AtoNum=[element["groupBlock"] for element in elements if element["symbol"]==query][0]
                        results.append({
                                    "Title": f"Group Block: {EleGrb_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleGrb_AtoNum] }
                                    })
                        EleSts_AtoNum=[element["standardState"] for element in elements if element["symbol"]==query][0]
                        results.append({
                                    "Title": f"Standard State: {EleSts_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleSts_AtoNum] }
                                    })
                        EleEcg_AtoNum=[element["electronegativity"] for element in elements if element["symbol"]==query][0]
                        results.append({
                                    "Title": f"Electronegativity: {EleEcg_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleNam_AtoNum] }
                                    })
                        EleAtr_AtoNum=[element["atomicRadius"] for element in elements if element["symbol"]==query][0]
                        results.append({
                                    "Title": f"Atomic Radius: {EleAtr_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleAtr_AtoNum] }
                                    })
                        EleIoR_AtoNum=[element["ionRadius"] for element in elements if element["symbol"]==query][0]
                        results.append({
                                    "Title": f"Ion Radius: {EleIoR_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleIoR_AtoNum] }
                                    })
                        EleVDR_AtoNum=[element["vanDerWaalsRadius"] for element in elements if element["symbol"]==query][0]
                        results.append({
                                    "Title": f"Van Der Waals Radius: {EleVDR_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleVDR_AtoNum] }
                                    })
                        EleIEn_AtoNum=[element["ionizationEnergy"] for element in elements if element["symbol"]==query][0]
                        results.append({
                                    "Title": f"Ionization Energy: {EleIEn_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleIEn_AtoNum] }
                                    })
                        EleEAf_AtoNum=[element["electronAffinity"] for element in elements if element["symbol"]==query][0]
                        results.append({
                                    "Title": f"Electron Affinity: {EleEAf_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleEAf_AtoNum] }
                                    })
                        EleBot_AtoNum=[element["bondingType"] for element in elements if element["symbol"]==query][0]
                        results.append({
                                    "Title": f"Bonding Type: {EleBot_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleBot_AtoNum] }
                                    })
                        EleMep_AtoNum=[element["meltingPoint"] for element in elements if element["symbol"]==query][0]
                        results.append({
                                    "Title": f"Melting Point: {EleMep_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleMep_AtoNum] }
                                    })
                        EleBop_AtoNum=[element["boilingPoint"] for element in elements if element["symbol"]==query][0]
                        results.append({
                                    "Title": f"Boiling Point: {EleBop_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleBop_AtoNum] }
                                    })
                        EleDen_AtoNum=[element["density"] for element in elements if element["symbol"]==query][0]
                        results.append({
                                    "Title": f"Density: {EleDen_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleDen_AtoNum] }
                                    })
                        EleDis_AtoNum=[element["yearDiscovered"] for element in elements if element["symbol"]==query][0]
                        results.append({
                                    "Title": f"Year Discovered: {EleDis_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleDis_AtoNum] }
                                    })
                        
                        EleCol_AtoNum=[element["cpkHexColor"] for element in elements if element["symbol"]==query][0]
                        results.append({
                                    "Title": f"Color: {EleCol_AtoNum}",
                                    "IcoPath": ImgCol,
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleCol_AtoNum] }
                                    })
                        
            elif query.isalpha and len(query) > 2:
                        if [element["cpkHexColor"] for element in elements if element["name"]==query][0] == "unknown":
                            ImgCol="Images/un.png"
                        else:
                            color_hex=[element["cpkHexColor"] for element in elements if element["name"]==query][0]
                            image(color_hex)
                            ImgCol=f"colors/{color_hex}.png"
    
                        EleNam_AtoNum=[element["name"] for element in elements if element["name"]==query][0]
                        results.append({
                                    "Title": f"Name: {EleNam_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleNam_AtoNum] }
                                    })
                        EleSym_AtoNum=[element["symbol"] for element in elements if element["name"]==query][0]
                        results.append({
                                    "Title": f"Symbol: {EleSym_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleSym_AtoNum] }
                                    })
                        EleNum_AtoNum=[element["atomicNumber"] for element in elements if element["name"]==query][0]
                        results.append({
                                    "Title": f"Atomic Number: {EleNum_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleNum_AtoNum] }
                                    })
                        EleMas_AtoNum=[element["atomicMass"] for element in elements if element["name"]==query][0]
                        results.append({
                                    "Title": f"Atomic Mass: {EleMas_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleMas_AtoNum] }
                                    })
                        ElePer_AtoNum=[element["period"] for element in elements if element["name"]==query][0]
                        results.append({
                                    "Title": f"Period: {ElePer_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [ElePer_AtoNum] }
                                    })
                        EleGer_AtoNum=[element["group"] for element in elements if element["name"]==query][0]
                        results.append({
                                    "Title": f"Group: {EleGer_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleGer_AtoNum] }
                                    })
                        EleBlo_AtoNum=[element["block"] for element in elements if element["name"]==query][0]
                        results.append({
                                    "Title": f"Block: {EleBlo_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleBlo_AtoNum] }
                                    })
                        EleCon_AtoNum=[element["electronicConfiguration"] for element in elements if element["name"]==query][0]
                        results.append({
                                    "Title": f"Electronic Configuration: {EleCon_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleCon_AtoNum] }
                                    })
                        EleOxi_AtoNum=[element["oxidationStates"] for element in elements if element["name"]==query][0]
                        results.append({
                                    "Title": f"Oxidation States: {EleOxi_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleOxi_AtoNum] }
                                    })
                        EleGrb_AtoNum=[element["groupBlock"] for element in elements if element["name"]==query][0]
                        results.append({
                                    "Title": f"Group Block: {EleGrb_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleGrb_AtoNum] }
                                    })
                        EleSts_AtoNum=[element["standardState"] for element in elements if element["name"]==query][0]
                        results.append({
                                    "Title": f"Standard State: {EleSts_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleSts_AtoNum] }
                                    })
                        EleEcg_AtoNum=[element["electronegativity"] for element in elements if element["name"]==query][0]
                        results.append({
                                    "Title": f"Electronegativity: {EleEcg_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleNam_AtoNum] }
                                    })
                        EleAtr_AtoNum=[element["atomicRadius"] for element in elements if element["name"]==query][0]
                        results.append({
                                    "Title": f"Atomic Radius: {EleAtr_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleAtr_AtoNum] }
                                    })
                        EleIoR_AtoNum=[element["ionRadius"] for element in elements if element["name"]==query][0]
                        results.append({
                                    "Title": f"Ion Radius: {EleIoR_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleIoR_AtoNum] }
                                    })
                        EleVDR_AtoNum=[element["vanDerWaalsRadius"] for element in elements if element["name"]==query][0]
                        results.append({
                                    "Title": f"Van Der Waals Radius: {EleVDR_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleVDR_AtoNum] }
                                    })
                        EleIEn_AtoNum=[element["ionizationEnergy"] for element in elements if element["name"]==query][0]
                        results.append({
                                    "Title": f"Ionization Energy: {EleIEn_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleIEn_AtoNum] }
                                    })
                        EleEAf_AtoNum=[element["electronAffinity"] for element in elements if element["name"]==query][0]
                        results.append({
                                    "Title": f"Electron Affinity: {EleEAf_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleEAf_AtoNum] }
                                    })
                        EleBot_AtoNum=[element["bondingType"] for element in elements if element["name"]==query][0]
                        results.append({
                                    "Title": f"Bonding Type: {EleBot_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleBot_AtoNum] }
                                    })
                        EleMep_AtoNum=[element["meltingPoint"] for element in elements if element["name"]==query][0]
                        results.append({
                                    "Title": f"Melting Point: {EleMep_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleMep_AtoNum] }
                                    })
                        EleBop_AtoNum=[element["boilingPoint"] for element in elements if element["name"]==query][0]
                        results.append({
                                    "Title": f"Boiling Point: {EleBop_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleBop_AtoNum] }
                                    })
                        EleDen_AtoNum=[element["density"] for element in elements if element["name"]==query][0]
                        results.append({
                                    "Title": f"Density: {EleDen_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleDen_AtoNum] }
                                    })
                        EleDis_AtoNum=[element["yearDiscovered"] for element in elements if element["name"]==query][0]
                        results.append({
                                    "Title": f"Year Discovered: {EleDis_AtoNum}",
                                    "IcoPath": "Images/app.png",
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleDis_AtoNum] }
                                    })
                        
                        EleCol_AtoNum=[element["cpkHexColor"] for element in elements if element["name"]==query][0]
                        results.append({
                                    "Title": f"Color: {EleCol_AtoNum}",
                                    "IcoPath": ImgCol,
                                    "JsonRPCAction": {"method": "copy", "parameters": [EleCol_AtoNum] }
                                    })
            else:
                 results.append({
                                    "Title": "Enter a valid value",
                                    "IcoPath": "Images/error.png"})
                                         
                
        except:
             results.append({
                            "Title": "Enter a valid value",
                            "IcoPath": "Images/error.png"})
             

        return results
    def copy(self, val):
        FlowLauncherAPI.show_msg("Copied to clipboard", copy2clip(val))    
if __name__ == "__main__":
    ElementFlow()
