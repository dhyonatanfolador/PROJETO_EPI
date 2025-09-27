# Sistema de Gerenciamento de EPIs (SGEPI)
## Introdução e Contextualização do Projeto
Este projeto consiste no desenvolvimento do Sistema de Gerenciamento de Equipamentos de Proteção Individual (SGEPI), uma solução digital proposta para a construtora [Nome da Construtora/Região]. O objetivo primário é mitigar a alta taxa de não utilização de EPIs por esquecimento ou falha na retirada, conforme identificado na auditoria interna.

O SGEPI visa digitalizar e controlar o ciclo de vida dos EPIs, desde o cadastro e fornecimento até a devolução, dano ou extravio, garantindo o cumprimento das normas de segurança e promovendo um ambiente de trabalho mais seguro.

## Casos de Uso do Sistema (SGEPI)

| ID   | Caso de Uso               | Ator Principal        | Descrição                                                                                                                                      |
|------|---------------------------|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| CU01 | Cadastrar Colaborador     | Técnico de Segurança  | Inclui novos funcionários no sistema, registrando informações básicas e sua foto.                                                              |
| CU02 | Gerenciar Colaborador     | Técnico de Segurança  | Permite a edição das informações ou a exclusão de um colaborador (com confirmação).                                                             |
| CU03 | Cadastrar Equipamento     | Técnico de Segurança  | Registra novos tipos de EPIs (ex: Capacete, Luva de Raspa) no inventário.                                                                       |
| CU04 | Gerenciar Equipamento     | Técnico de Segurança  | Permite a edição das informações ou a exclusão de um EPI do inventário.                                                                         |
| CU05 | Realizar Controle de EPI  | Técnico de Segurança  | Registra a entrega de um EPI a um colaborador, definindo a data de empréstimo/fornecimento e a previsão de devolução.                           |
| CU06 | Atualizar Status de EPI   | Técnico de Segurança  | Atualiza o status de um item emprestado para Devolvido, Danificado ou Perdido, registrando a data e observações.                                |
| CU07 | Gerar Relatórios          | Técnico de Segurança  | Filtra e visualiza o histórico de empréstimos/fornecimentos por colaborador, equipamento e status.                                               |

## Requisitos do Sistema
### Requisitos Funcionais (RF)
| ID   | Requisito Funcional       | Descrição                                                                                                                                                  |
|------|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RF01 | Gestão de Colaboradores   | O sistema deve permitir o CRUD (Criação, Leitura, Atualização e Exclusão) de colaboradores.                                                                |
| RF02 | Gestão de EPIs            | O sistema deve permitir o CRUD (Criação, Leitura, Atualização e Exclusão) de equipamentos de proteção individual.                                           |
| RF03 | Controle de Empréstimo    | O sistema deve registrar a entrega de EPIs com data de empréstimo, previsão de devolução, status e chaves estrangeiras para Colaborador e Equipamento.      |
| RF04 | Restrições de Status      | O sistema deve exibir apenas os status Emprestado e Fornecido no cadastro, e todos os status (Devolvido, Danificado, Perdido) na edição.                    |
| RF05 | Campos Condicionais       | Os campos "Data da devolução" e "Observação na devolução" devem aparecer apenas na edição, ao selecionar os status Dev./Dan./Per.                          |
| RF06 | Relatórios Detalhados     | O sistema deve gerar relatórios com filtros (tipo AND) por nome do colaborador, nome do equipamento e status.                                               |
| RF07 | Restrição na Edição       | Na atualização de status, os campos Colaborador, Equipamento, Data do Empréstimo e Data Prevista da Devolução devem ser desabilitados (disabled).           |
| RF08 | Feedback ao Usuário       | O sistema deve exibir mensagens de sucesso ou falha (utilizando Bootstrap) em todas as operações de cadastro e atualização.                                 |


### Requisitos Não Funcionais (RNF)
| ID    | Requisito Não Funcional | Descrição                                                                                                 |
|-------|--------------------------|-----------------------------------------------------------------------------------------------------------|
| RNF01 | Usabilidade              | A interface do sistema deve ser intuitiva, utilizando a biblioteca Bootstrap para um design responsivo e moderno. |
| RNF02 | Segurança                | O sistema deve garantir a integridade e consistência dos dados (Ex: Uso de chaves estrangeiras para relacionamentos). |
| RNF03 | Desempenho               | As consultas de relatórios e a navegação entre telas devem ser rápidas e eficientes.                      |
| RNF04 | Plataforma               | O sistema será desenvolvido em Python/Django, seguindo as diretrizes de instalação do projeto.             |

## Guia de Instalação e Execução
O sistema SGEPI foi desenvolvido utilizando o framework Django (Python).
### 1. Pré-requisitos
Certifique-se de ter o Python instalado em sua máquina.
### 2. Clonagem do Repositório
Abra o terminal e clone o projeto:

```
Bash
git clone 'link-repositorio'
cd nome-do-projeto
```

### 3. Instalação das Dependências
Instale o framework Django e o Pillow (necessário para o upload de fotos dos colaboradores):

```
Bash
python -m pip install Django
python -m pip install pillow
```

### (Opcional) Atualizar o pip:

```
Bash
python -m pip install --upgrade pip
```

### 4. Configuração Inicial e Migrações
Antes de rodar, é preciso aplicar as migrações iniciais do banco de dados:

```
Bash
python .\manage.py makemigrations
python .\manage.py migrate
```

### 5. Execução do Servidor
Para iniciar o sistema, execute o servidor de desenvolvimento:

```
Bash
python .\manage.py runserver
```
O sistema estará acessível em http://127.0.0.1:8000/.

# Estrutura de Codificação (Skeletons HTML/Django)
Abaixo estão exemplos de como estruturar as telas usando Bootstrap, seguindo a lógica de backend do Django.

## 2.1. Tela Base (Estrutura com Menu Lateral)
Este ```base.html``` deve ser a estrutura principal, que será estendida pelas outras telas.

```
HTML

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>SGEPI</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .sidebar { height: 100vh; width: 250px; position: fixed; top: 0; left: 0; padding-top: 56px; }
        .content { margin-left: 250px; padding: 20px; }
        .user-info { padding: 15px; text-align: center; border-bottom: 1px solid #444; }
        .user-photo { width: 60px; height: 60px; object-fit: cover; border-radius: 50%; margin-bottom: 5px; }
    </style>
</head>
<body>
    <div class="sidebar bg-dark text-white">
        <div class="user-info">
            <img src="/static/img/user_default.png" alt="Foto do Usuário" class="user-photo border border-white">
            <p class="mb-0 fw-bold">Técnico João Silva</p>
            <small class="text-muted">Setor: Segurança do Trabalho</small>
        </div>
        
        <ul class="nav flex-column mt-3">
            <li class="nav-item"><a class="nav-link text-white" href="{% url 'home' %}">Início</a></li>
            <li class="nav-item"><a class="nav-link text-white" href="{% url 'colaborador_cadastro' %}">Cadastro de Colaboradores</a></li>
            <li class="nav-item"><a class="nav-link text-white" href="{% url 'equipamento_cadastro' %}">Cadastro de Equipamentos</a></li>
            <li class="nav-item"><a class="nav-link text-white" href="{% url 'controle_epi_cadastro' %}">Controle de EPI</a></li>
            <li class="nav-item"><a class="nav-link text-white" href="{% url 'relatorios' %}">Relatórios</a></li>
        </ul>
    </div>

    <div class="content">
        {% block content %}
        {% endblock %}
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    {% block scripts %}{% endblock %}
</body>
</html>
```

### 2.2. Tela Cadastro de Colaboradores (Exemplo)
```
HTML

{% extends "base.html" %}

{% block content %}
    <h2>Cadastro de Novo Colaborador</h2>

    {% if messages %}
        {% for message in messages %}
            <div class="alert alert-{{ message.tags }} alert-dismissible fade show" role="alert">
                {{ message }}
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
        {% endfor %}
    {% endif %}

    <form method="POST" enctype="multipart/form-data">
        {% csrf_token %}
        <div class="mb-3">
            <label for="id_nome" class="form-label">Nome Completo</label>
            <input type="text" class="form-control" id="id_nome" name="nome" required>
        </div>
        
        <div class="mb-3">
            <label for="id_foto" class="form-label">Foto do Colaborador</label>
            <input type="file" class="form-control" id="id_foto" name="foto" accept="image/*">
        </div>

        <button type="submit" class="btn btn-success">Cadastrar Colaborador</button>
        <a href="{% url 'colaborador_listagem' %}" class="btn btn-secondary">Ver Listagem</a>
    </form>

{% endblock %}
```
### 2.3. Tela de Controle de EPI (Cadastro Inicial)
Esta tela deve conter apenas os status Emprestado e Fornecido.
```
HTML

{% extends "base.html" %}

{% block content %}
    <h2>Controle de Entrega de EPI</h2>
    
    <form method="POST">
        {% csrf_token %}
        <div class="row">
            <div class="col-md-6 mb-3">
                <label for="id_colaborador" class="form-label">Colaborador</label>
                <select class="form-select" id="id_colaborador" name="colaborador_id" required>
                    <option value="" selected disabled>Selecione o Colaborador</option>
                    <option value="1">Colaborador A</option> 
                    </select>
            </div>
            
            <div class="col-md-6 mb-3">
                <label for="id_equipamento" class="form-label">Equipamento</label>
                <select class="form-select" id="id_equipamento" name="equipamento_id" required>
                    <option value="" selected disabled>Selecione o Equipamento</option>
                    <option value="1">Capacete de Segurança</option>
                    </select>
            </div>

            <div class="col-md-6 mb-3">
                <label for="id_data_entrega" class="form-label">Data da Entrega/Empréstimo</label>
                <input type="date" class="form-control" id="id_data_entrega" name="data_entrega" value="{{ hoje }}" required>
            </div>
            
            <div class="col-md-6 mb-3">
                <label for="id_data_prevista_devolucao" class="form-label">Data Prevista p/ Devolução</label>
                <input type="date" class="form-control" id="id_data_prevista_devolucao" name="data_prevista_devolucao" required>
            </div>

            <div class="col-md-12 mb-3">
                <label for="id_status" class="form-label">Status Inicial</label>
                <select class="form-select" id="id_status" name="status" required>
                    <option value="Emprestado">Emprestado</option>
                    <option value="Fornecido">Fornecido</option>
                </select>
            </div>
        </div>

        <button type="submit" class="btn btn-primary">Registrar Entrega de EPI</button>
    </form>
{% endblock %}
```
### 2.4. Tela de Controle de EPI (Edição/Atualização de Status)
Esta é a tela de edição, onde os campos de identificação são desabilitados e os campos de devolução são exibidos condicionalmente.
```
HTML

{% extends "base.html" %}

{% block content %}
    <h2>Atualizar Status do EPI (ID: {{ item_controle.pk }})</h2>
    
    <form method="POST">
        {% csrf_token %}
        <div class="row">
            <div class="col-md-6 mb-3">
                <label class="form-label">Colaborador</label>
                <input type="text" class="form-control" value="{{ item_controle.colaborador.nome }}" disabled>
                </div>
            <div class="col-md-6 mb-3">
                <label class="form-label">Equipamento</label>
                <input type="text" class="form-control" value="{{ item_controle.equipamento.nome }}" disabled>
            </div>
            <div class="col-md-6 mb-3">
                <label class="form-label">Data do Empréstimo</label>
                <input type="date" class="form-control" value="{{ item_controle.data_entrega|date:'Y-m-d' }}" disabled>
            </div>
            <div class="col-md-6 mb-3">
                <label class="form-label">Data Prevista Devolução</label>
                <input type="date" class="form-control" value="{{ item_controle.data_prevista_devolucao|date:'Y-m-d' }}" disabled>
            </div>
            <div class="col-md-12 mb-3">
                <label for="id_status_edit" class="form-label">Novo Status</label>
                <select class="form-select" id="id_status_edit" name="status" required>
                    <option value="Emprestado" {% if item_controle.status == 'Emprestado' %}selected{% endif %}>Emprestado</option>
                    <option value="Fornecido" {% if item_controle.status == 'Fornecido' %}selected{% endif %}>Fornecido</option>
                    <option value="Devolvido" {% if item_controle.status == 'Devolvido' %}selected{% endif %}>Devolvido</option>
                    <option value="Danificado" {% if item_controle.status == 'Danificado' %}selected{% endif %}>Danificado</option>
                    <option value="Perdido" {% if item_controle.status == 'Perdido' %}selected{% endif %}>Perdido</option>
                </select>
            </div>

            <div id="devolucao_fields" style="display: none;">
                <div class="col-md-6 mb-3">
                    <label for="id_data_devolucao" class="form-label">Data da Devolução</label>
                    <input type="date" class="form-control" id="id_data_devolucao" name="data_devolucao" value="{{ item_controle.data_devolucao|date:'Y-m-d' }}">
                </div>
                <div class="col-md-6 mb-3">
                    <label for="id_obs_devolucao" class="form-label">Observação na Devolução</label>
                    <textarea class="form-control" id="id_obs_devolucao" name="observacao_devolucao">{{ item_controle.observacao_devolucao }}</textarea>
                </div>
            </div>
            </div>

        <button type="submit" class="btn btn-warning">Atualizar Status</button>
    </form>
{% endblock %}

{% block scripts %}
<script>
    document.addEventListener('DOMContentLoaded', function() {
        const statusSelect = document.getElementById('id_status_edit');
        const devFields = document.getElementById('devolucao_fields');
        const camposDevolucao = ['Devolvido', 'Danificado', 'Perdido'];

        function toggleDevolucaoFields() {
            if (camposDevolucao.includes(statusSelect.value)) {
                devFields.style.display = 'block';
            } else {
                devFields.style.display = 'none';
            }
        }

        // Executa na carga inicial
        toggleDevolucaoFields(); 
        
        // Executa na mudança de status
        statusSelect.addEventListener('change', toggleDevolucaoFields);
    });
</script>
{% endblock %}
```
### 2.5. Tela de Relatórios (Com Filtro AND)
```
HTML

{% extends "base.html" %}

{% block content %}
    <h2>Relatórios de Controle de EPI</h2>

    <form method="GET" class="mb-4 border p-3 bg-light">
        <h5 class="mb-3">Filtros de Pesquisa (Tipo AND)</h5>
        <div class="row">
            <div class="col-md-4 mb-3">
                <label for="filtro_colaborador" class="form-label">Nome do Colaborador</label>
                <input type="text" class="form-control" id="filtro_colaborador" name="colaborador" value="{{ request.GET.colaborador }}">
            </div>
            <div class="col-md-4 mb-3">
                <label for="filtro_equipamento" class="form-label">Nome do Equipamento</label>
                <input type="text" class="form-control" id="filtro_equipamento" name="equipamento" value="{{ request.GET.equipamento }}">
            </div>
            <div class="col-md-4 mb-3">
                <label for="filtro_status" class="form-label">Status</label>
                <select class="form-select" id="filtro_status" name="status">
                    <option value="">Todos</option>
                    <option value="Emprestado" {% if request.GET.status == 'Emprestado' %}selected{% endif %}>Emprestado</option>
                    <option value="Fornecido" {% if request.GET.status == 'Fornecido' %}selected{% endif %}>Fornecido</option>
                    <option value="Devolvido" {% if request.GET.status == 'Devolvido' %}selected{% endif %}>Devolvido</option>
                    <option value="Danificado" {% if request.GET.status == 'Danificado' %}selected{% endif %}>Danificado</option>
                    <option value="Perdido" {% if request.GET.status == 'Perdido' %}selected{% endif %}>Perdido</option>
                </select>
            </div>
        </div>
        <button type="submit" class="btn btn-primary">Aplicar Filtros</button>
        <a href="{% url 'relatorios' %}" class="btn btn-outline-secondary">Limpar Filtros</a>
    </form>
    
    <table class="table table-striped table-hover">
        <thead>
            <tr>
                <th>Colaborador</th>
                <th>Equipamento</th>
                <th>Data Empréstimo</th>
                <th>Prev. Devolução</th>
                <th>Status</th>
                <th>Ações</th>
            </tr>
        </thead>
        <tbody>
            {% for item in resultados %}
            <tr>
                <td>{{ item.colaborador.nome }}</td>
                <td>{{ item.equipamento.nome }}</td>
                <td>{{ item.data_entrega|date:"d/m/Y" }}</td>
                <td>{{ item.data_prevista_devolucao|date:"d/m/Y" }}</td>
                <td>
                    <span class="badge 
                        {% if item.status == 'Emprestado' %}bg-warning text-dark
                        {% elif item.status == 'Devolvido' %}bg-success
                        {% elif item.status == 'Danificado' or item.status == 'Perdido' %}bg-danger
                        {% else %}bg-info
                        {% endif %}">
                        {{ item.status }}
                    </span>
                </td>
                <td>
                    <a href="{% url 'controle_epi_editar' item.pk %}" class="btn btn-sm btn-info">Editar Status</a>
                </td>
            </tr>
            {% empty %}
            <tr>
                <td colspan="6" class="text-center">Nenhum registro encontrado com os filtros aplicados.</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>

{% endblock %}
```
### Próximos Passos:

1. **Modelo Django:** Crie os modelos (```Colaborador```, ```Equipamento```, ```ControleEPI```) no ```models.py``` para as chaves estrangeiras.
2. **Views Django:** Implemente as funções (views) para processar os formulários (```POST```) e renderizar as telas (```GET```), gerenciando o feedback (mensagens de sucesso/falha).
3. **URLs:** Defina as rotas (URLs) que linkam o menu lateral com as views.
4. **Gravação e Slides:** Prepare o slide, insira esta documentação e grave a tela mostrando a funcionalidade completa (Cadastro → Controle → Edição de Status → Relatórios).
