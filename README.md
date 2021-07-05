# Controle de Medicamentos

Disponibilização de ambiente em *Docker* para o sistema *WEB* básico de controle de medicamentos desenvolvido em *Python* com o *Framework Django*.

## Sobre

A interface e comportamento do sistema são idênticos aos presentes em [php-medication_controller](https://github.com/lucasrafael/php-medication_controller), diferenciando apenas nas tecnologias utilizadas.

Este contém basicamente:
- Python;
- Django.

O outro:
- PHP;
- Laravel.

Os detalhes de funcionamento podem ser obtidos na página inicial do sistema citado.

### Motivação

O objetivo de refazer o mesmo sistema com outras tecnologias foi verificar quais seriam as vantagens e desvantagens no processo de desenvolvimento.

### Abordagem de desenvolvimento

Este projeto também foi desenvolvido com *Docker* (arquivo de configuração *Dockerfile*) e *docker-compose* (arquivo de configuração *docker-compose.yml*); e o banco de dados utilizado também foi o **SQLite**.

#### Instalados por meio do *Docker* 

- **Python** (versão *3.8*);
- **Django** (versão *3.2.4*);
- **DateTime** (versão *4.3*);
- **PyYAML** (versão *5.4.1*).

### Preparação do ambiente

1. Baixar projeto do GitHub:
```sh
git clone https://github.com/lucasrafael/python-medication_controller.git
```

2. Construção do ambiente e inicialização:
```sh
docker-compose up --build
```

### Comandos úteis

- Preenchimento das tabelas com alguns dados para testes (opção **-it** para modo interativo): 
```sh
docker exec -it <CONTAINER_ID> python manage.py loaddata dados-iniciais.yaml
```

- Compilação das mensagens presentenes em **app/locale/**, caso tenham sido previamente modificadas:
```sh
docker exec -it <CONTAINER_ID> django-admin compilemessages --settings=locale
```

- Criação de usuário **admin**, caso seja necessário, para manipular com a interface administrativa:
```sh
docker exec -it <CONTAINER_ID> python manage.py createsuperuser
```
