# AWS-Santander

## Desafio: Implementar uma Infraestrutura Automatizada em Nuvem com AWS CloudFormation

> O projeto “Implementando Infraestrutura Automatizada com AWS CloudFormation” tem como objetivo demonstrar como a Infraestrutura como Código (IaC) pode ser aplicada na automação do provisionamento de recursos na nuvem AWS.

---

### Descrição do Projeto:

Por meio do AWS CloudFormation, é possível descrever toda a infraestrutura de um ambiente em um template no formato YAML ou JSON, permitindo que os recursos sejam criados de maneira padronizada e controlada.
Essa abordagem elimina tarefas manuais repetitivas e reduz falhas, garantindo consistência em todos os ambientes de desenvolvimento, testes e produção.

---

### Objetivo:

O principal objetivo deste projeto é apresentar a teoria por trás da automação de infraestrutura na AWS, destacando:

- O conceito de Infraestrutura como Código (IaC);
- O papel do CloudFormation na orquestração de recursos;
- As vantagens de automatizar a criação de ambientes em nuvem;
- A importância da padronização e versionamento de templates.

---

### Conceitos Fundamentais:

**1. Infraestrutura como Código (IaC)**

A IaC é uma prática de DevOps que permite gerenciar e provisionar recursos de TI por meio de arquivos de configuração legíveis por humanos, em vez de processos manuais.
Com isso, a infraestrutura torna-se versão-controlada, automatizada e reutilizável.

**2. AWS CloudFormation**

O CloudFormation é um serviço da AWS que interpreta arquivos de configuração (templates) para criar, atualizar e excluir recursos automaticamente.
Esses templates descrevem todos os componentes necessários, como redes, servidores, bancos de dados e permissões.

**3. Stacks e Resources no AWS CloudFormation**

No AWS CloudFormation, os stacks (pilhas) representam a unidade lógica de provisionamento da infraestrutura.
Uma stack é composta por um conjunto de recursos e aplicações definidos em um template, sendo todos criados, atualizados e excluídos como uma única unidade.
Isso garante que todos os componentes permaneçam em um estado consistente, reduzindo erros e simplificando o gerenciamento da infraestrutura.

Os resources (recursos), por sua vez, são os elementos individuais da infraestrutura — como instâncias EC2, buckets S3, VPCs, subnets, funções IAM, entre outros — que são criados e configurados automaticamente a partir do template.

**3.1. Estados da Stack**

CREATE_IN_PROGRESS: Recursos sendo provisionados

CREATE_COMPLETE: Stack criada com sucesso

CREATE_FAILED: Erro na criação, rollback automático

UPDATE_IN_PROGRESS: Stack sendo atualizada

DELETE_IN_PROGRESS: Recursos sendo removidos

**4. Template YAML**

O template YAML funciona como um “mapa” da infraestrutura. Ele contém seções que definem:

- Parameters – valores configuráveis para personalizar o stack;
- Resources – recursos que serão criados (VPC, EC2, S3, IAM, etc.);
- Outputs – informações exibidas ao final da implantação;
- Mappings e Conditions – lógicas condicionais e variações regionais.

**5. Template JSON**

O template JSON também funciona como um “mapa” da infraestrutura, descrevendo de forma estruturada e hierárquica todos os recursos que compõem o ambiente na nuvem.
Ele é baseado em pares de chave e valor, utilizando colchetes { } para objetos e colchetes [ ] para listas.

Assim como o YAML, ele contém seções que definem:

- Parameters – valores configuráveis que permitem personalizar o stack, como tipo da instância, nome da VPC ou par de chaves.
- Resources – recursos que serão criados e configurados (VPC, EC2, S3, IAM, etc.).
- Outputs – informações retornadas ao final da implantação, como IP público, ID da instância ou nome do bucket.
- Mappings e Conditions – lógicas condicionais e variações regionais que adaptam o comportamento do template.

O formato JSON é mais técnico e rigoroso em sua sintaxe, exigindo o uso correto de aspas duplas, vírgulas e chaves.
Por outro lado, oferece alta compatibilidade com linguagens de programação e ferramentas AWS, sendo amplamente utilizado em automações e pipelines.

| Aspecto                   | JSON                                            | YAML                                     |
| ------------------------- | ----------------------------------------------- | ---------------------------------------- |
| **Legibilidade**          | Mais técnico, ideal para sistemas automatizados | Mais limpo e legível para humanos        |
| **Sintaxe**               | Exige aspas, vírgulas e chaves explícitas       | Baseado em indentação e dois-pontos      |
| **Erros comuns**          | Falta de vírgula ou aspas                       | Indentação incorreta                     |
| **Uso em CloudFormation** | Suportado oficialmente desde o início           | Versão mais moderna e preferida pela AWS |
| **Conversão**             | Fácil de converter para YAML e vice-versa       | Compatível com JSON                      |


---

### Componentes da Infraestrutura:

Em um projeto teórico como este, a arquitetura proposta contempla os seguintes elementos:

- VPC (Virtual Private Cloud) – rede privada virtual que abriga os recursos;
- Subnets – subdivisões da VPC, podendo ser públicas ou privadas;
- Internet Gateway – permite a comunicação entre a VPC e a internet;
- Route Tables – controlam o roteamento do tráfego de rede;
- Security Groups – atuam como firewalls virtuais;
- Instância EC2 – máquina virtual configurada automaticamente;
- S3 Bucket – armazenamento de arquivos e logs;
- IAM Roles e Policies – controle de permissões e acessos.

---

### Benefícios da Automação com CloudFormation:

**- Padronização:** garante que todos os ambientes sejam idênticos.

**- Reprodutibilidade:** infraestrutura pode ser recriada em minutos.

**- Escalabilidade:** fácil replicação e ajuste conforme a demanda.

**- Segurança:** controle detalhado de permissões e acesso.

**- Economia de tempo:** elimina tarefas manuais e propensas a erro.

**- Versionamento:** possibilidade de armazenar templates em repositórios Git.

---

### Ciclo de Vida da Automação:

**- Modelagem:** definição dos recursos e suas dependências no template YAML.

**- Provisionamento:** o CloudFormation lê o arquivo e cria o stack correspondente.

**- Gerenciamento:** monitoramento e atualização dos recursos de forma centralizada.

**- Rollback:** caso ocorra erro, o serviço reverte automaticamente as alterações.

---

### Boas Práticas:

1. Utilizar nomes descritivos para recursos e parâmetros.

2. Adicionar comentários e descrições nos templates YAML.

3. Armazenar templates em controle de versão (ex: GitHub).

4. Aplicar o princípio de least privilege para permissões IAM.

5. Validar templates antes da execução com o comando `aws cloudformation validate-template`.

---

### Diferença entre AWS CloudFormation e Terraform

| Característica | **AWS CloudFormation** | **Terraform** |
|----------------|------------------------|----------------|
| **Provedor** | Exclusivo da AWS | Multicloud (AWS, Azure, GCP etc.) |
| **Linguagem** | YAML ou JSON | HCL (HashiCorp Configuration Language) |
| **Gerenciamento de estado** | Controlado automaticamente pela AWS | Estado armazenado localmente ou em repositório remoto |
| **Integração com AWS** | Nativa e mais profunda | Boa, mas via APIs externas |
| **Custos** | Gratuito (paga-se apenas pelos recursos criados) | Gratuito (open-source) |
| **Curva de aprendizado** | Mais simples para quem usa só AWS | Mais flexível, mas exige mais configuração |

### Quando usar qual?

Use CloudFormation se:

- Seu ambiente for 100% AWS
- Você deseja integração nativa com os serviços da AWS
- Prefere não gerenciar arquivos de estado manualmente

Use Terraform se:

- Você trabalha com múltiplos provedores de nuvem
- Deseja mais controle sobre o ciclo de vida dos recursos
- Precisa de reutilização avançada com módulos e melhor controle de dependências
---

### Conclusão:

O uso do AWS CloudFormation representa uma evolução na forma como as organizações constroem e mantêm suas infraestruturas na nuvem.
Por meio da Infraestrutura como Código, é possível obter agilidade, consistência e controle, além de facilitar o trabalho em equipe e a escalabilidade dos ambientes.

Essa prática é fundamental dentro do contexto de DevOps e Cloud Computing, sendo amplamente adotada em projetos modernos que exigem eficiência operacional e automação.