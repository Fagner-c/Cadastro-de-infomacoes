from tkinter import *
usuarios = list()
#Carcteristicas da Janela:
def janela_caracteristicas():
    #Tamanho e posição da janela:
    janela_largura= 800
    janela_altura= 700
    tela_largura = janela.winfo_screenwidth()
    tela_altura= janela.winfo_screenheight()
    posx= tela_largura / 2 - janela_largura/2 
    posy= tela_altura/2 - janela_altura/2
    janela.geometry('%dx%d+%d+%d' %(janela_largura, janela_altura, posx, posy))
    #Nome, cor, respansividade , icone e removendo barra de titulo:
    janela.title('Cadastro de Usuarios')
    janela.resizable(False, False)
    janela.config(background='#1C1C1C', borderwidth=6, relief='solid')
    janela.iconbitmap('imagens/icone.ico')
#Montando Desiner:
def janela_desiner():
    #Frame Principal:
    f1 = Frame(janela, background='#1C1C1C', width=750, height=650 )
    f1.place(rely=0.03, relx= 0.03)
    #Label Do Cadastro:
    inicio_f1 = Label(f1, text='Cadastro de Usuarios', font='Arial, 18',foreground= '#FFFAFA', background='#1C1C1C').place(relx=0.34, rely=0.05)
    frame_cadastro = Frame(f1, background='#1C1C1C', width=600, height=500)
    frame_cadastro.place(relx=0.06, rely=0.1)
    #Label dos campos:
    user_nome_lb = Label(frame_cadastro, text='Nome ', background='#1C1C1C', font='Arial, 12', foreground='#FFFAFA').place(relx= 0.02, rely= 0.05)
    user_idade_lb = Label(frame_cadastro, text='Idade ', background='#1C1C1C', font='Arial, 12', foreground='#FFFAFA').place(relx= 0.56, rely= 0.05)
    user_cpf_lb = Label(frame_cadastro, text='Cpf ', background='#1C1C1C', font='Arial, 12', foreground='#FFFAFA').place(relx= 0.02, rely= 0.1)
    user_endereco_lb = Label(frame_cadastro, text='Endereço ', background='#1C1C1C', font='Arial, 12', foreground='#FFFAFA').place(relx= 0.56, rely= 0.1)
    user_profissao_lb = Label(frame_cadastro, text='Profissão ', background='#1C1C1C', font='Arial, 12', foreground='#FFFAFA').place(relx= 0.02, rely= 0.15)
    user_email_lb = Label(frame_cadastro, text='Email ', background='#1C1C1C', font='Arial, 12', foreground='#FFFAFA').place(relx= 0.56, rely= 0.15)
    #Campos de entrada:
    user_entry = Entry(frame_cadastro, width=25)
    user_entry.place(relx=0.16, rely=0.058)
    idade_entry = Entry(frame_cadastro, width=25)
    idade_entry.place(relx=0.72, rely=0.055)
    cpf_entry = Entry(frame_cadastro, width=25)
    cpf_entry.place(relx=0.16, rely=0.108)
    endereco_entry = Entry(frame_cadastro, width=25)
    endereco_entry.place(relx=0.72, rely=0.105)
    profissao_entry = Entry(frame_cadastro, width=25)
    profissao_entry.place(relx=0.16, rely=0.158)
    email_entry = Entry(frame_cadastro, width=25)
    email_entry.place(relx=0.72, rely=0.155)
    #Botão de cadastro e função de cadastro:
    def cadastrar_usuario():
        label_info.destroy()
        user = user_entry.get()
        idade = idade_entry.get()
        cpf = cpf_entry.get()
        endereco = endereco_entry.get()
        profissao = profissao_entry.get()
        email = email_entry.get() 
        valor = [user, idade, cpf, endereco, profissao, email]
        for val in valor:
            if not val:
                val = False
                break   
        if val == False: 
            info_cadastro(label_info, frame_cadastro, 'Existe campos não preenchidos!', '#FF0000')
        else:
            if '@gmail' in email:
                try:
                    if len(cpf) == 11:
                        cpf = int(cpf)
                        try:
                            idade = int(idade)
                            if idade > 0:
                                info_cadastro(label_info, frame_cadastro, 'Usuario adicionado com sucesso!', '#32CD32')
                                conta_usuario = {'nome' : user, 'idade' : idade, 'cpf': cpf, 'endereço' : endereco, 'profissão' : profissao, 'email' : email}
                                usuarios.append(conta_usuario)
                                user_entry.delete(0, END)
                                idade_entry.delete(0, END)
                                cpf_entry.delete(0, END)
                                endereco_entry.delete(0, END)
                                profissao_entry.delete(0, END)
                                email_entry.delete(0, END)
                                f1.destroy()
                                janela_desiner()
                            else:
                                info_cadastro(label_info, frame_cadastro, 'A idade digitada não é valida!', '#FF0000')
                        except:
                            info_cadastro(label_info, frame_cadastro, 'A idade digitada não é valida!', '#FF0000')
                    else:
                        info_cadastro(label_info, frame_cadastro,  'Cpf deve ter 11 digitos!', '#FF0000')
                except: 
                    info_cadastro(label_info, frame_cadastro, 'Cpf só pode ter numeros!', '#FF0000')
            else:
                info_cadastro(label_info, frame_cadastro, 'O email digitado não é valido!', '#FF0000')
    bnt_cadastro = Button(frame_cadastro,text='Cadastrar', font='Arial, 12', foreground='#FFFAFA', background= '#363636',padx=60, command=cadastrar_usuario)
    bnt_cadastro.place(relx=0.15, rely=0.31)
    #Local para verificação de erro:
    label_info = Frame(frame_cadastro,background='#1C1C1C', width=350, height=20)
    label_info.place(relx=0.22, rely=0.25)
    def info_cadastro(local, framep, texto, cor):
        local = Frame(framep,background='#1C1C1C', width=350, height=20)
        local.place(relx=0.22, rely=0.25)
        erro = Message(local, text=texto, background='#1C1C1C', font='Arial, 8', foreground= cor, width=300)
        erro.place(relx=0.29)
    #Botão e função para ver as pessoas cadastras:
    def verificar_usuario():
        #atualizando o Frame principal: 
        f1.destroy()
        f2 = Frame(janela, background='#1C1C1C', width=750, height=600)
        f2.place(relx=0.03, rely=0.05)
        #Perssonalizando no Frame principál:
        inicio_f2 = Label(f2, text='Usuarios cadastrados', font='Arial, 18',foreground= '#FFFAFA', background='#1C1C1C').place(relx=0.34, rely=0.05)
        frame_exibir =Frame(f2,background='#1C1C1C', width=720, height=500)
        frame_exibir.place(rely=0.15)
        #Criando a menssagem para exibir usuarios existentes:
        users =''
        cont = 0
        if not usuarios:
            users = 'Não foi adicionado nenhum ainda!'
        else:
            for user in usuarios:
                cont += 1
                texto = f"{cont}-Nome: {user['nome']} | Idade: {user['idade']} | Cpf: {user['cpf']} | Endereço: {user['endereço']} | Profissão: {user['profissão']} | Email: {user['email']}\n"
                users += texto
        #Exibindo os usuarios:
        exibindo = Label(frame_exibir,text = users ,font='Arial, 8', background='#1C1C1C', foreground='#FFFAFA')
        exibindo.place(relx=0.05, rely=0.01)
        #Botão Voltar e função voltar:
        def volta_inicio():
            f2.destroy()
            janela_desiner()
        bnt_voltar_inicio = Button(f2, text='Inicio', font='Arial, 12', foreground='#FFFAFA', background= '#363636',padx=60, command=volta_inicio)
        bnt_voltar_inicio.place(relx=0.19, rely=0.8)
        #Botão para limpar lista:
        def limpar():
            usuarios.clear()
            f2.destroy()
            verificar_usuario()
        bnt_limpar_lista = Button(f2, text='Limpar lista', font='Arial, 12', foreground='#FFFAFA', background= '#363636',padx=40, command=limpar)
        bnt_limpar_lista.place(relx=0.49, rely=0.8)
    bnt_verificar_cadastro = Button(frame_cadastro,text='Verificar Cadastrados', font='Arial, 12', foreground='#FFFAFA', background= '#363636',padx=20, command=verificar_usuario)
    bnt_verificar_cadastro.place(relx=0.53, rely=0.31)
    #Adicionando tabela de ultimos adicionados:
    frame_ultimo_adicionado = Frame(f1,background="#1C1C1C", width=750, height=170, borderwidth=3, relief='solid')
    frame_ultimo_adicionado.place(rely=0.7)
    #Adicionando os ultimos:
    if len(usuarios) == 1:
        txt_ultimo_lb = Label(frame_ultimo_adicionado, text='Ultimos adicionados: ',  font='Arial, 9',foreground= '#FFFAFA', background='#1C1C1C').place(relx=0.02, rely=0.1)
        ultimo1_lb = Label(frame_ultimo_adicionado, text=f"Nome: {usuarios[-1]['nome']} | Email: {usuarios[-1]['email']} | Cpf: {usuarios[-1]['cpf']}",  font='Arial, 9',foreground= '#FFFAFA', background='#1C1C1C').place(relx=0.02, rely=0.3)
    elif len(usuarios) > 1:
        txt_ultimo_lb = Label(frame_ultimo_adicionado, text='Ultimos adicionados: ',  font='Arial, 9',foreground= '#FFFAFA', background='#1C1C1C').place(relx=0.02, rely=0.1)
        ultimo1_lb = Label(frame_ultimo_adicionado,text=f"Nome: {usuarios[-1]['nome']} | Email: {usuarios[-1]['email']} | Cpf: {usuarios[-1]['cpf']}",  font='Arial, 9',foreground= '#FFFAFA', background='#1C1C1C').place(relx=0.02, rely=0.3)
        ultimo2_lb = Label(frame_ultimo_adicionado, text=f"Nome: {usuarios[-2]['nome']} | Email: {usuarios[-2]['email']} | Cpf: {usuarios[-2]['cpf']}", font='Arial, 9',foreground= '#FFFAFA', background='#1C1C1C').place(relx=0.02, rely=0.6)
    else:
        ultimo1_lb = Label(frame_ultimo_adicionado, text='Nenhum adicionado ainda',  font='Arial, 9',foreground= '#FFFAFA', background='#1C1C1C').place(relx= 0.02,rely=0.1)
#Execultando janela e suas funções:
janela = Tk()
janela_caracteristicas()
janela_desiner()
janela.mainloop()