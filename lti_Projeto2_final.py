import tkinter as tk
import requests
import json
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np



# Define the API endpoint
ip =""
port =""
url = ""
#url example = "http://192.168.159.144:8001/api/v1/"

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("microK8S")
        self.geometry("1000x800")
        
        self.frames = {}
        
        # create and add the frames to a dictionary
        for F in (StartPage,
        PageDashboard,
        PageNodes,
        PageNamespaces,PageNamespaces_Listar,PageNamespaces_Criar,PageNamespaces_Apagar,
        PagePods,PagePods_Listar,PagePods_Criar,PagePods_Apagar,
        PageDeployments,PageDeployments_Listar,PageDeployments_Criar,PageDeployments_Apagar,
        PageServices,PageServices_Listar,PageServices_Criar,PageServices_Apagar):
            frame = F(self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(StartPage)
        
    def show_frame(self, page):
        """Show a frame for the given page"""
        frame = self.frames[page]
        frame.tkraise()
        
class StartPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        #self.entry_text = tk.StringVar()
        
        #entry = tk.Entry(self, textvariable=self.entry_text)
        #entry.pack(pady=5, padx=10)
        label = tk.Label(self, text="This is the start page")
        label.pack(pady=10, padx=10)

        label = tk.Label(self, text="ip:")
        label.pack(pady=10, padx=10)

        global ip_Text
        ip_Text = tk.Text(self,height = 1, width = 20)
        ip_Text.pack()

        label = tk.Label(self, text="port:")
        label.pack(pady=10, padx=10)

        global port_Text
        port_Text = tk.Text(self,height = 1, width = 20)
        port_Text.pack()

        
        button_Submit = tk.Button(self, text="Submit", command=submit_text)
        button_Submit.pack(pady=5, padx=10)

        global StartPage_display_text
        StartPage_display_text = tk.Label(self, text="")
        StartPage_display_text.pack(pady=10, padx=10)

        button_interfaces = tk.Button(self, text="Dashboard", command=lambda: master.show_frame(PageDashboard))
        button_interfaces.pack()
        
        button_interfaces = tk.Button(self, text="informações dos Nodes", command=lambda: master.show_frame(PageNodes))
        button_interfaces.pack()

        button_Namespaces = tk.Button(self, text="Pagina de Namespaces", command=lambda: master.show_frame(PageNamespaces))
        button_Namespaces.pack()

        button_Namespaces = tk.Button(self, text="Pagina de Pods", command=lambda: master.show_frame(PagePods))
        button_Namespaces.pack()

        button_Namespaces = tk.Button(self, text="Pagina de Deployments", command=lambda: master.show_frame(PageDeployments))
        button_Namespaces.pack()

        button_Namespaces = tk.Button(self, text="Pagina de PageServices", command=lambda: master.show_frame(PageServices))
        button_Namespaces.pack()
#___________________________________________________________________________________________________________________________________________________________________
class PageDashboard(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="pagina: informações dos Dashboard")
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text='Listar todas as informações dos Dashboard', command=listarDashboard)
        button.pack()

        global response_label_Dashboard
        response_label_Dashboard = tk.Text(self)
        response_label_Dashboard.pack()
        
        button1 = tk.Button(self, text="Go to Start Page", command=lambda: [delete_text(),master.show_frame(StartPage)])
        button1.pack()

#___________________________________________________________________________________________________________________________________________________________________
    
class PageNodes(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="pagina: informações dos Nodes")
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text='Listar todas as informações dos Nodes', command=listarInfoNodes)
        button.pack()

        global response_label
        response_label = tk.Text(self)
        response_label.pack()
        
        button1 = tk.Button(self, text="Go to Start Page", command=lambda: [delete_text(),master.show_frame(StartPage)])
        button1.pack() 
#___________________________________________________________________________________________________________________________________________________________________

class PageNamespaces(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        

        button = tk.Button(self, text="listar todos os Namespaces", command=lambda:[master.show_frame(PageNamespaces_Listar)])
        button.pack()

        button = tk.Button(self, text="criar um Namespace", command=lambda:[master.show_frame(PageNamespaces_Criar)])
        button.pack()

        button = tk.Button(self, text="apagar um Namespace", command=lambda:[master.show_frame(PageNamespaces_Apagar)])
        button.pack()

        button = tk.Button(self, text="Go to Start Page", command=lambda:[master.show_frame(StartPage)])
        button.pack() 

class PageNamespaces_Listar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="pagina: listar todos os Namespaces")
        label.pack(pady=10, padx=10)

        button_listar_Bridges = tk.Button(self, text='listar todos os Namespaces', command=listarNamespaces)
        button_listar_Bridges.pack()

        global response_label_Namespaces
        response_label_Namespaces = tk.Text(self)
        response_label_Namespaces.pack()

        
        button = tk.Button(self, text="Go Back", command=lambda:[delete_text_Namespaces_Listar(),master.show_frame(PageNamespaces)])
        button.pack()

class PageNamespaces_Criar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="Nome de Namespace:")
        label.pack(pady=10, padx=10)

        global Namespace_Name_Text
        Namespace_Name_Text = tk.Text(self,height = 1, width = 20)
        Namespace_Name_Text.pack()

        
        button_Submit_Namespaces_Criar = tk.Button(self, text="Submit", command=submit_Namespaces_Criar)
        button_Submit_Namespaces_Criar.pack(pady=5, padx=10)
        
        button = tk.Button(self, text="Go Back", command=lambda:[master.show_frame(PageNamespaces)])
        button.pack()

class PageNamespaces_Apagar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="Nome de Namespace para apagar:")
        label.pack(pady=10, padx=10)

        global Namespace_Name_Text_Get_Delete
        Namespace_Name_Text_Get_Delete = tk.Text(self,height = 1, width = 20)
        Namespace_Name_Text_Get_Delete.pack()
        
        button_Submit_Namespace_Delete = tk.Button(self, text="Submit", command=Delete_Namespace)
        button_Submit_Namespace_Delete.pack(pady=5, padx=10)

        #global StartPage_display_text
        #StartPage_display_text = tk.Label(self, text="")
        #StartPage_display_text.pack(pady=10, padx=10)         Meter O OK se for 200

        
        button = tk.Button(self, text="Go Back", command=lambda:[master.show_frame(PageNamespaces)])
        button.pack()

        #___________________________________________________________________________________________________________________________________________________________________

class PagePods(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        

        button = tk.Button(self, text="listar todos os Pods", command=lambda:[master.show_frame(PagePods_Listar)])
        button.pack()

        button = tk.Button(self, text="Criar Pod", command=lambda:[master.show_frame(PagePods_Criar)])
        button.pack()

        button = tk.Button(self, text="Apagar Pod", command=lambda:[master.show_frame(PagePods_Apagar)])
        button.pack()

        button = tk.Button(self, text="Go to Start Page", command=lambda:[master.show_frame(StartPage)])
        button.pack() 

class PagePods_Listar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="pagina: listar todos os Pods")
        label.pack(pady=10, padx=10)

        button_listar_Bridges = tk.Button(self, text='listar todos os Pods', command=listarPods)
        button_listar_Bridges.pack()

        global response_label_Pods
        response_label_Pods = tk.Text(self)
        response_label_Pods.pack()

        
        button = tk.Button(self, text="Go Back", command=lambda:[master.show_frame(PagePods)])
        button.pack()

class PagePods_Criar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="Nome de Namespace:")
        label.pack(pady=10, padx=10)

        global Namespace_Create_Name_Text
        Namespace_Create_Name_Text = tk.Text(self,height = 1, width = 20)
        Namespace_Create_Name_Text.pack()

        label = tk.Label(self, text="Nome da imagem para instalar:")
        label.pack(pady=10, padx=10)

        global Pod_Create_image_Name_Text
        Pod_Create_image_Name_Text = tk.Text(self,height = 1, width = 20)
        Pod_Create_image_Name_Text.pack()

        label = tk.Label(self, text="versão:\n(no caso de não meter nenhuma vai ser latest)")
        label.pack(pady=10, padx=10)

        global Pod_Create_image_versio_Name_Text
        Pod_Create_image_versio_Name_Text = tk.Text(self,height = 1, width = 20)
        Pod_Create_image_versio_Name_Text.pack()

        label = tk.Label(self, text="container port:")
        label.pack(pady=10, padx=10)

        global Pod_Create_Container_Port_Text
        Pod_Create_Container_Port_Text = tk.Text(self,height = 1, width = 20)
        Pod_Create_Container_Port_Text.pack()

        label = tk.Label(self, text="Host port:")
        label.pack(pady=10, padx=10)

        global Pod_Create_Host_Port_Text
        Pod_Create_Host_Port_Text = tk.Text(self,height = 1, width = 20)
        Pod_Create_Host_Port_Text.pack()

        
        button_Submit_Namespaces_Criar = tk.Button(self, text="Submit", command=submit_Pods_Criar)
        button_Submit_Namespaces_Criar.pack(pady=5, padx=10)
        
        button = tk.Button(self, text="Go Back", command=lambda:[master.show_frame(PagePods)])
        button.pack()

class PagePods_Apagar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        label = tk.Label(self, text="Nome do Namespace onde esta o Pod a apagar:")
        label.pack(pady=10, padx=10)

        global Pod_Nmapespace_Text_Get_Delete
        Pod_Nmapespace_Text_Get_Delete = tk.Text(self,height = 1, width = 20)
        Pod_Nmapespace_Text_Get_Delete.pack()
        
        label = tk.Label(self, text="Nome do Pod a apagar:")
        label.pack(pady=10, padx=10)

        global Pod_Name_Text_Get_Delete
        Pod_Name_Text_Get_Delete = tk.Text(self,height = 1, width = 20)
        Pod_Name_Text_Get_Delete.pack()
        
        button_Submit_Pod_Delete = tk.Button(self, text="Submit", command=Delete_Pod)
        button_Submit_Pod_Delete.pack(pady=5, padx=10)

        #global StartPage_display_text
        #StartPage_display_text = tk.Label(self, text="")
        #StartPage_display_text.pack(pady=10, padx=10)         Meter O OK se for 200

        
        button = tk.Button(self, text="Go Back", command=lambda:[master.show_frame(PagePods)])
        button.pack()
#____________________________________________________________________________________________________________________________________________________________
class PageDeployments(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        

        button = tk.Button(self, text="listar todos os Deployments", command=lambda:[master.show_frame(PageDeployments_Listar)])
        button.pack()

        button = tk.Button(self, text="criar Deployment", command=lambda:[master.show_frame(PageDeployments_Criar)])
        button.pack()

        button = tk.Button(self, text="apagar Deployment", command=lambda:[master.show_frame(PageDeployments_Apagar)])
        button.pack()

        button = tk.Button(self, text="Go to Start Page", command=lambda:[master.show_frame(StartPage)])
        button.pack() 

class PageDeployments_Listar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="pagina: listar todos os Deployments")
        label.pack(pady=10, padx=10)

        button_listar_Bridges = tk.Button(self, text='listar todos os Deployments', command=listarDeployments)
        button_listar_Bridges.pack()

        global response_label_Deployments
        response_label_Deployments = tk.Text(self)
        response_label_Deployments.pack()

        
        button = tk.Button(self, text="Go Back", command=lambda:[master.show_frame(PageDeployments)])
        button.pack()

class PageDeployments_Criar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="Nome de Namespace:")
        label.pack(pady=10, padx=10)

        global Deplayment_Create_Name_Text
        Deplayment_Create_Name_Text = tk.Text(self,height = 1, width = 20)
        Deplayment_Create_Name_Text.pack()

        label = tk.Label(self, text="Numero de replicas:")
        label.pack(pady=10, padx=10)

        global Deplayment_Create_replicas_Text
        Deplayment_Create_replicas_Text = tk.Text(self,height = 1, width = 20)
        Deplayment_Create_replicas_Text.pack()

        label = tk.Label(self, text="Nome da imagem para instalar:")
        label.pack(pady=10, padx=10)

        global Deplayment_Create_image_Name_Text
        Deplayment_Create_image_Name_Text = tk.Text(self,height = 1, width = 20)
        Deplayment_Create_image_Name_Text.pack()

        label = tk.Label(self, text="versão:\n(no caso de não meter nenhuma vai ser latest)")
        label.pack(pady=10, padx=10)

        global Deplayment_Create_image_versao_Name_Text
        Deplayment_Create_image_versao_Name_Text = tk.Text(self,height = 1, width = 20)
        Deplayment_Create_image_versao_Name_Text.pack()

        label = tk.Label(self, text="container port:")
        label.pack(pady=10, padx=10)

        global Deplayment_Create_Container_Port_Text
        Deplayment_Create_Container_Port_Text = tk.Text(self,height = 1, width = 20)
        Deplayment_Create_Container_Port_Text.pack()

        label = tk.Label(self, text="Host port:")
        label.pack(pady=10, padx=10)

        global Deplayment_Create_Host_Port_Text
        Deplayment_Create_Host_Port_Text = tk.Text(self,height = 1, width = 20)
        Deplayment_Create_Host_Port_Text.pack()

        

        button_Submit_Deployment_Criar = tk.Button(self, text="Submit", command=submit_Deployment_Criar)
        button_Submit_Deployment_Criar.pack(pady=5, padx=10)
        
        button = tk.Button(self, text="Go Back", command=lambda:[master.show_frame(PageDeployments)])
        button.pack()

class PageDeployments_Apagar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        label = tk.Label(self, text="Nome do Namespace onde esta o Deployment a apagar:")
        label.pack(pady=10, padx=10)

        global Deployment_Nmapespace_Text_Get_Delete
        Deployment_Nmapespace_Text_Get_Delete = tk.Text(self,height = 1, width = 20)
        Deployment_Nmapespace_Text_Get_Delete.pack()
        
        label = tk.Label(self, text="Nome do Deployment a apagar:")
        label.pack(pady=10, padx=10)

        global Deployment_Name_Text_Get_Delete
        Deployment_Name_Text_Get_Delete = tk.Text(self,height = 1, width = 20)
        Deployment_Name_Text_Get_Delete.pack()
        
        button_Submit_Pod_Delete = tk.Button(self, text="Submit", command=Delete_Deployment)
        button_Submit_Pod_Delete.pack(pady=5, padx=10)

        #global StartPage_display_text
        #StartPage_display_text = tk.Label(self, text="")
        #StartPage_display_text.pack(pady=10, padx=10)         Meter O OK se for 200

        
        button = tk.Button(self, text="Go Back", command=lambda:[master.show_frame(PageDeployments)])
        button.pack()
#____________________________________________________________________________________________________________________________________________________________

class PageServices(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        

        button = tk.Button(self, text="listar todos os Services", command=lambda:[master.show_frame(PageServices_Listar)])
        button.pack()

        button = tk.Button(self, text="criar Service", command=lambda:[master.show_frame(PageServices_Criar)])
        button.pack()

        button = tk.Button(self, text="apagar Service", command=lambda:[master.show_frame(PageServices_Apagar)])
        button.pack()

        button = tk.Button(self, text="Go to Start Page", command=lambda:[master.show_frame(StartPage)])
        button.pack() 

class PageServices_Listar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="pagina: listar todos os Services")
        label.pack(pady=10, padx=10)

        button_listar_Bridges = tk.Button(self, text='listar todos os Services', command=listarServices)
        button_listar_Bridges.pack()

        global response_label_Services
        response_label_Services = tk.Text(self)
        response_label_Services.pack()

        
        button = tk.Button(self, text="Go Back", command=lambda:[master.show_frame(PageServices)])
        button.pack()

class PageServices_Criar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="Nome do Service:")
        label.pack(pady=10, padx=10)

        global Service_Name_Text
        Service_Name_Text = tk.Text(self,height = 1, width = 20)
        Service_Name_Text.pack()

        label = tk.Label(self, text="Namespace:")
        label.pack(pady=10, padx=10)

        global Service_Namespace_Text
        Service_Namespace_Text = tk.Text(self,height = 1, width = 20)
        Service_Namespace_Text.pack()

        label = tk.Label(self, text="Protocol:")
        label.pack(pady=10, padx=10)

        global Service_Protocol_Text
        Service_Protocol_Text = tk.Text(self,height = 1, width = 20)
        Service_Protocol_Text.pack()

        label = tk.Label(self, text="Port:")
        label.pack(pady=10, padx=10)

        global Service_Port_Text
        Service_Port_Text = tk.Text(self,height = 1, width = 20)
        Service_Port_Text.pack()

        label = tk.Label(self, text="Target Port:")
        label.pack(pady=10, padx=10)

        global Service_TargetPort_Text
        Service_TargetPort_Text = tk.Text(self,height = 1, width = 20)
        Service_TargetPort_Text.pack()

        
        button_Submit_Services_Criar = tk.Button(self, text="Submit", command=submit_Services_Criar)
        button_Submit_Services_Criar.pack(pady=5, padx=10)
        
        button = tk.Button(self, text="Go Back", command=lambda:[master.show_frame(PageServices)])
        button.pack()

class PageServices_Apagar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="Nome de service para apagar:")
        label.pack(pady=10, padx=10)

        global Service_Name_Text_Get_Delete
        Service_Name_Text_Get_Delete = tk.Text(self,height = 1, width = 20)
        Service_Name_Text_Get_Delete.pack()

        label = tk.Label(self, text="Nome do namespace:")
        label.pack(pady=10, padx=10)

        global Service_Namespace_Text_Get_Delete
        Service_Namespace_Text_Get_Delete = tk.Text(self,height = 1, width = 20)
        Service_Namespace_Text_Get_Delete.pack()
        
        button_Submit_Service_Delete = tk.Button(self, text="Submit", command=Delete_Service)
        button_Submit_Service_Delete.pack(pady=5, padx=10)

        #global StartPage_display_text
        #StartPage_display_text = tk.Label(self, text="")
        #StartPage_display_text.pack(pady=10, padx=10)         Meter O OK se for 200

        
        button = tk.Button(self, text="Go Back", command=lambda:[master.show_frame(PageServices)])
        button.pack()


#____________________________________________________________________________________________________________________________________________________________

##FUNCOES--------------------------------------------------------------------------
def submit_text():
    """Update the display label with the entered text"""
    global ip
    ip = ip_Text.get("1.0","end-1c")
    global port
    port = port_Text.get("1.0","end-1c")
    global url
    #http://192.168.126.130:8001/api/v1/
    if port == "" or url == "":
        url = "http://192.168.159.144:8001/"
    else:
        url = "http://"+ip+":"+port+"/"
  
    StartPage_display_text.config(text=url)
    #text = entry_text.get()
    #display_text.config(text=text)

def listarDashboard():
    global url
    response = requests.get(url + "apis/metrics.k8s.io/v1beta1/nodes", verify=False)
    response_data = response.json()

    devolver = ""

    cpu_values = []
    memory_values = []
    node_names = []

    def convert_to_millicores(value, unit):
        if unit == 'm':
            return float(value)
        elif unit == 'u':
            return float(value) / 1000
        elif unit == 'n':
            return float(value) / 1000000
        else:
            return 0
        
    for i in range(len(response_data['items'])):
        devolver = devolver + (
            "Nome: " + response_data['items'][i]['metadata']['name'] + "\n" + "OS: " +
            response_data['items'][i]['metadata']['labels']['kubernetes.io/os'] + "\n" + "CPU: " +
            response_data['items'][i]['usage']['cpu'] + "      memory:" + response_data['items'][i]['usage'][
                'memory'] + "\n" + "_________________________________________________________________" + "\n")
  
        cpu_usage_raw = response_data['items'][i]['usage']['cpu']
        cpu_unit = cpu_usage_raw[-1]  # Extract the unit ('m', 'u', or 'n')
        cpu_usage = convert_to_millicores(cpu_usage_raw[:-1], cpu_unit)
        
        node_name = str(response_data['items'][i]['metadata']['name'])
        memory_value = float(response_data['items'][i]['usage']['memory'].strip('Ki'))

        response2 = requests.get(url+"api/v1/nodes/"+node_name,verify=False)
        response_data2 = response2.json()

        cpu_capacity_aux = response_data2['status']['capacity']['cpu'] 
        cpu_capacity = float(cpu_capacity_aux[-1]) * 1000

        memory_capacity = float(response_data2['status']['capacity']['memory'].strip('Ki'))

        cpu_percentage = (float(cpu_usage) / float(cpu_capacity)) * 100
        memory_percentage = (memory_value / memory_capacity) * 100


        node_names.append(node_name)
        cpu_values.append(cpu_percentage)
        memory_values.append(memory_percentage)

    response_label_Dashboard.delete('1.0', 'end')
    response_label_Dashboard.insert('end', devolver)

    fig, ax = plt.subplots()
    width = 0.35

    ax.clear()
    x = np.arange(len(node_names))
    # Plot the memory bars
    ax.bar(x - width/2, memory_values, width, label='Memory')

    ax.bar(x + width/2, cpu_values, width, label='CPU')
    ax.set_xlabel('Node')
    ax.set_ylabel('Usage (%)')
    ax.set_title('CPU and Memory Usage per Node')
    ax.legend()
    ax.set_xticks(x)
    ax.set_xticklabels(node_names)
    plt.show()




def listarInfoNodes():       
    global url
    response = requests.get(url+"api/v1/nodes",verify=False)
    response_data = response.json()

    devolver = ""
    for i in range(len(response_data['items'])):
        #print("Nome: "+response_data['items'][i]['metadata']['name'])
        #print("Cpu: "+response_data['items'][i]['status']['capacity']['cpu'])
        #print("Spcae: "+response_data['items'][i]['status']['capacity']['ephemeral-storage'])
        #print("RAM: "+response_data['items'][i]['status']['capacity']['memory'])
        #print("__________________________________________________________________")
    #print(list(map(lambda x: x['metadata']['name'], response_data['items'])))

        gb_Spcae_to_int = response_data['items'][i]['status']['capacity']['ephemeral-storage'][:-2]
        gb_Spcae = int(gb_Spcae_to_int) / (1024 * 1024)

        gb_RAM_to_int = response_data['items'][i]['status']['capacity']['memory'][:-2]
        gb_RAM = int(gb_RAM_to_int) / (1024 * 1024)
        
        devolver = devolver + ("Nome: "+response_data['items'][i]['metadata']['name']+"\n"+"Cpu: "+response_data['items'][i]['status']['capacity']['cpu']+"\n"+"Spcae: "+response_data['items'][i]['status']['capacity']['ephemeral-storage']+" = "+str(gb_Spcae)+"GB"+"\n"+"RAM: "+response_data['items'][i]['status']['capacity']['memory']+" = "+str(gb_RAM)+"GB"+"\n"+"__________________________________________________________________"+"\n")

    response_label.delete('1.0', 'end')
    response_label.insert('end', devolver)

def delete_text():
    response_label.delete("1.0","end-1c")   
#_________________________________________________________________________________________________________________________________________________________________
def listarNamespaces():
        
    global url
    response = requests.get(url+"api/v1/namespaces",verify=False)
    response_data = response.json()

    devolver = ""

    for i in range(len(response_data['items'])):
         devolver = devolver + ("Nome: "+response_data['items'][i]['metadata']['name']+"\n"+"labels: "+response_data['items'][i]['metadata']['labels']['kubernetes.io/metadata.name']+"\n"+"phase: "+response_data['items'][i]['status']['phase']+"\n"+"time: "+response_data['items'][i]['metadata']['managedFields'][0]['time']+"\n"+"_________________________________________________________________"+"\n")

    response_label_Namespaces.delete('1.0', 'end')
    response_label_Namespaces.insert('end', devolver)

def delete_text_Namespaces_Listar():
    response_label_Namespaces.delete("1.0","end-1c")



def submit_Namespaces_Criar():
    global url

    Name = Namespace_Name_Text.get("1.0","end-1c")
    print(Name)
    payload = {
                "apiVersion": "v1",
                "kind": "Namespace",
                "metadata": {
                 "name": Name
                            }
                }
    json_payload = json.dumps(payload)
    headers = {"Content-Type": "application/json"}

    response = requests.post(url+"api/v1/namespaces",headers=headers,data=json_payload,verify=False)
    response_data = response.json()

    print(response.status_code)

def Delete_Namespace():     
    global url
    response = requests.get(url+"api/v1/namespaces",verify=False)
    response_data = response.json()
    Name = Namespace_Name_Text_Get_Delete.get("1.0","end-1c")
    ID_a_mudar = ""
    #print(Name)
    for i in range(len(response_data['items'])):
        if response_data['items'][i]['metadata']['name'] == str(Name):
            ID_a_mudar = response_data['items'][i]['metadata']['name']
            print(Name)
    #print(url+"namespaces\\"+ID_a_mudar)
    response = requests.delete(url+"api/v1/namespaces/"+ID_a_mudar,verify=False)
    print(response.status_code)

    

#________________________________________________________________________________________________________________________________________________________


def listarPods():
        
    global url
    response = requests.get(url+"api/v1/pods",verify=False)
    response_data = response.json()

    devolver = ""

    for i in range(len(response_data['items'])):
         devolver = devolver + ("Nome: "+response_data['items'][i]['metadata']['name']+"\n"+"image: "+response_data['items'][i]['spec']['containers'][0]['image']+"\n"+"node: "+response_data['items'][i]['spec']['nodeName']+"\n"+"status: "+response_data['items'][i]['status']['phase']+"\n"+"time: "+response_data['items'][i]['metadata']['creationTimestamp']+"\n"+"_________________________________________________________________"+"\n")

    response_label_Pods.delete('1.0', 'end')
    response_label_Pods.insert('end', devolver)

def submit_Pods_Criar():
    global url
    Name = Namespace_Create_Name_Text.get("1.0","end-1c")
    Image = Pod_Create_image_Name_Text.get("1.0","end-1c")

    if Pod_Create_image_versio_Name_Text.get("1.0","end-1c") == "":
        version = "latest"
    else:
        version = Pod_Create_image_versio_Name_Text.get("1.0","end-1c")

    
    Container_port = Pod_Create_Container_Port_Text.get("1.0","end-1c")
    Host_port = Pod_Create_Host_Port_Text.get("1.0","end-1c")

    print(Name)
    print(Image)
    print(version)
    print(Container_port)
    print(Host_port)
    


    #print(Name) #80 #8080
    payload ={
  "apiVersion": "v1",
  "kind": "Pod",
  "metadata": {
    "name": Name+"-"+Image
  },
  "spec": {
    "containers": [
      {
        "name": "nginx-container",
        "image": Image+":"+version,
        "ports": [
          {
            "containerPort": int(Container_port),
            "hostPort": int(Host_port)
          }
        ]
      }
    ]
  }
} 
    json_payload = json.dumps(payload)
    headers = {"Content-Type": "application/json"}

    response = requests.post(url+"api/v1/namespaces/"+Name+"/pods",headers=headers,data=json_payload,verify=False)
    response_data = response.json()

    print(response.status_code)

def Delete_Pod():        
    global url

    
    Pod_namespace = Pod_Nmapespace_Text_Get_Delete.get("1.0","end-1c") #teste1
    Name = Pod_Name_Text_Get_Delete.get("1.0","end-1c")                #teste1-nginx

    
    print(Name)
    print(Pod_namespace)

    response = requests.delete(url+"api/v1/namespaces/"+Pod_namespace+"/pods/"+Name,verify=False)
    print(response.status_code)

#________________________________________________________________________________________________________________________________________________________

def listarDeployments():
        
    global url
    response = requests.get(url+"apis/apps/v1/deployments",verify=False)
    response_data = response.json()

    devolver = ""

    for i in range(len(response_data['items'])):
         devolver = devolver + ("Nome: "+response_data['items'][i]['metadata']['name']+"\n"+"image: "+response_data['items'][i]['spec']['template']['spec']['containers'][0]['image']+"\n"+"Pods: "+str(response_data['items'][i]['spec']['replicas'])+"\n"+"time: "+response_data['items'][i]['metadata']['creationTimestamp']+"\n"+"_________________________________________________________________"+"\n")

    response_label_Deployments.delete('1.0', 'end')
    response_label_Deployments.insert('end', devolver)


def submit_Deployment_Criar():
    global url
    Name = Deplayment_Create_Name_Text.get("1.0","end-1c")

    #Num_replicas = Deplayment_Create_replicas_Text.get("1.0","end-1c")
    if Deplayment_Create_replicas_Text.get("1.0","end-1c") == "":
        Num_replicas = "1"
    else:
        Num_replicas = Deplayment_Create_replicas_Text.get("1.0","end-1c")

    Image = Deplayment_Create_image_Name_Text.get("1.0","end-1c")
 

    if Deplayment_Create_image_versao_Name_Text.get("1.0","end-1c") == "":
        version = "latest"
    else:
        version = Deplayment_Create_image_versao_Name_Text.get("1.0","end-1c")
    
    Container_port = Deplayment_Create_Container_Port_Text.get("1.0","end-1c")
    Host_port = Deplayment_Create_Host_Port_Text.get("1.0","end-1c")


    #print(Name)
    payload ={
  "apiVersion": "apps/v1",
  "kind": "Deployment",
  "metadata": {
    "name": Name+"-"+Image
  },
  "spec": {
    "replicas": int(Num_replicas),
    "selector": {
      "matchLabels": {
        "app": "nginx-web1"
      }
    },
    "template": {
      "metadata": {
        "labels": {
          "app": "nginx-web1"
        }
      },
      "spec": {
        "containers": [
          {
            "name": "nginx-web1",
            "image": Image+":"+version,
            "ports": [
              {
                "name": "http",
                "containerPort": int(Container_port),
                "hostPort": int(Host_port)
              }
            ]
          }
        ]
      }
    }
  }
}



    json_payload = json.dumps(payload)
    headers = {"Content-Type": "application/json"}

    response = requests.post(url+"apis/apps/v1/namespaces/"+Name+"/deployments",headers=headers,data=json_payload,verify=False)
    response_data = response.json()

    print(response.status_code)


def Delete_Deployment():        
    global url
 
    Deployment_namespace = Deployment_Nmapespace_Text_Get_Delete.get("1.0","end-1c") #teste1
    Name = Deployment_Name_Text_Get_Delete.get("1.0","end-1c")                #teste1-nginx

    
    print(Name)
    print(Deployment_namespace)

    response = requests.delete(url+"apis/apps/v1/namespaces/"+Deployment_namespace+"/deployments/"+Name,verify=False)
    print(response.status_code)

#__________________________________________________________________________________________________________________________________________________________
def listarServices():
        
    global url
    response = requests.get(url+"api/v1/services",verify=False)
    response_data = response.json()

    devolver = ""

    for i in range(len(response_data['items'])):
         devolver = devolver + ("Nome: "+response_data['items'][i]['metadata']['name']+"\n"+"Type: "+response_data['items'][i]['spec']['type']+"\n"+"ClusterIP: "+response_data['items'][i]['spec']['clusterIP']+"\n"+"Internal Endpoints: "+str(response_data['items'][i]['spec']['ports'][0]['port'])+" "+str(response_data['items'][i]['spec']['ports'][0]['protocol']) +"\n"+"time: "+response_data['items'][i]['metadata']['creationTimestamp']+"\n"+"_________________________________________________________________"+"\n")

    response_label_Services.delete('1.0', 'end')
    response_label_Services.insert('end', devolver)

def submit_Services_Criar():
    global url

    Name = Service_Name_Text.get("1.0","end-1c")
    protocol = Service_Protocol_Text.get("1.0","end-1c")
    port1 = Service_Port_Text.get("1.0","end-1c")
    targetPort = Service_TargetPort_Text.get("1.0","end-1c")
    Namespace = Service_Namespace_Text.get("1.0","end-1c")
    print(Name)
    payload = {
               "apiVersion": "v1",
               "kind": "Service",
               "metadata": {
                   "name": Name,
                   "namespace": Namespace
                   },
               "spec": {
                   "ports": [
                        {
                         "protocol": protocol,
                         "port": int(port1),
                         "targetPort": int(targetPort)
                        }
                   ],
                  "type": "ClusterIP"
                 }
               }
    json_payload = json.dumps(payload)
    headers = {"Content-Type": "application/json"}

    response = requests.post(url+"api/v1/namespaces/"+Namespace+"/services",headers=headers,data=json_payload,verify=False)
    response_data = response.json()

    print(response.status_code)
    
def Delete_Service():     
    global url  
    namespace = Service_Namespace_Text_Get_Delete.get("1.0","end-1c")
    Name = Service_Name_Text_Get_Delete.get("1.0","end-1c")
    
    response = requests.delete(url+"api/v1/namespaces/"+namespace+"/services/"+Name,verify=False)
    print(response.status_code)
#__________________________________________________________________________________________________________________________________________________________   



if __name__ == "__main__":
    app = MyApp()
    app.mainloop()

