# Gerenciador de Pedido 
## (order manager)

## 🐍 python project

### This repository contains all files needed for the aplication to run.
## ⬇️ Installing
It's very simple, you just need to download this repository, after unzipping the folder you can just open the certa3.exe and the application should run correctly.

## 🧩 Usage
### ⛵ navigating
As a CLI (Command Line Interface) application, there is no clicking, just typing. The main menu is composed with 13 options, every option has It's own character in front of it, you must type it and press `ENTER` in order to access that funcionatally. For example, if you wan't to access `Criar pedido` (create order) you must type `1` and then press `ENTER` so then you can access that option.

### 🧮 System logic
This system consist basically on the orders, so it's order centered, but the financial system (balance, entries and exits) runs in parallel, so if you conclude an order you must manually add it as an entry. The main MENU is diveded in 3 principal areas as you can see on your screen: CAIXA (cashier), GERENCIAMENTO DE PEDIDO (Order management) and HISTORICO (history), above the main Menu you have the current value on the cashier.
### CAIXA (cashier)
On this section you have 2 options (E)Entradas (entries) and (S)Saidas (exits), pressing E or S will direct you to a screen where you can type the value in reais.
### GERENCIAMENTO DE PEDIDO (order management)
On this section are all the needed operations to manage an order, you can (1)create, (2)edit, (3)consult order, (4)consult on going orders, (5)remove order and (6)conclude an order.
#### Creating an order
To create an order it's very simple, on the main menu you just press `1` and press `ENTER`, after that you are already describing the order to the system, you will describe the following informations respectively:
* NUMERO (order number) 
* NOME (client name)
* TELEFONE (client phone)
* PEÇAS (unitary number of products your client want's you to work on, fixing or selling)
* DESCRIÇÃO (description, here you can describe anything about the order and write down some consideration to yourself as well)
* DATA DE ENTREGA (deliver date, have in mind this is a string field, so you can write literally everything on it)
* PAGAMENTO (paying method)
* TOTAL (How it's going to cost as a total)
After filliing those fields all the order informations will be displayed on the screen so you can check if everything is correct, either way you press `ENTER` and if your order has some wrong information, you can edit it.
#### Managing an order
After creating your order you can consult it, it will search by the order number, phone or name. You can even consult all the orders on going, it will display some briefs informations about every order, you can remove it, if for some reason you dont need more this register, and you can conclude and order.
#### Concluding an order
It's so simple as creating an order, you press `6` and then press `ENTER`, you must write the number of the order you want to conclude and press `ENTER` again. All the concluded order will be displayed on the (7)Pedidos option on the HISTORICO section.
### HISTORICO (history)
On this section you have all the history of your system you can access (7)Pedidos (orders) for orders history, (8)Entradas (entries) for entries history, (9)Saídas (exits for exits history and (0)Balanço (balanace) for balance history.


## Description
This is a CLI (Command Line Interface) order manager for local stores wich stores the information locally, this application it's intended to help small shop owners organize their customers and financial data. It was programmed in procedural method, so if you are willing to modify this code for your usage, be ready. By now there is no classes, only functions, all code is contained in one file called `certa3.py`. If you, somehow, ended up on this repository and are interested on helping this project, feel free to contribute with the idea, I use this repository for studying, but more importantly for small shop owners, I know this isn't enough for them right now, but as soon as I work on some updates I expect to make an application that really can help small shops manage their orders, storing information locally by now.

##Documentation
Most of this code is programmed in portuguese, below are some important translation and all the description needed to comprehend the application's files.
#### 📄 Files
#### balanco.txt
(balanco = balance)
This text file contains every information about EXITS and ENTRIES of the cashier.
#### entrada.txt
(entrada = entries)
This text file contains all ENTRIES registered on the system.
#### saida.txt
(saida = exit)
Such as `entrada.txt`, this file contains all the EXITS registered on the system.
#### pedidos.json
(pedidos = orders)
This `JSON` it's the main data structure for the system, delete or wipe it out completely and you won't be able to run the application anymore (yes, the application won't work if this file is empty. I'll fix it). Here are contained all the ON GOING orders on your system, orders that are not CONCLUDED.
#### historico.json
(historico = history)
This `JSON` just like `pedidos.json` contains crucial information for the system, just like `pedidos.json` if this archive is wiped out or deleted, your application won't work. Here are conteined all the CONCLUDED orders.
#### certa3.py
Here are all the scripts for the system to work, this is a procedural script so all it's functionality is contained below the `# Main` commentary, the scripts basically upgrade those JSONs files before the user input (if you application open but closes instantly, probally this is where it's is failing, if the system can't read any information contained on those JSONs files so it can't start, I will fix it), after that the system is a `while` loop until you type `Q` and press `ENTER`.

## 📣 On Coming 
### Major update
* Changing to local web application
* probally changing script to an OOP method




This repository is very important for me, it was my first project intended to be a real solution, it gave me a lot of insights and sure those codes are very basic and amateur, but it's not only about the code, but how I could help my mother with my knowledge.
