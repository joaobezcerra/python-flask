# PythonFlask

Este projeto de e-commerce utiliza Python e o microframework Flask para criar uma plataforma online de vendas robusta e escalável. O principal objetivo é fornecer uma solução completa para gerenciamento de produtos, usuários, carrinho de compras e transações.

# Autenticação e Autorização de Usuários

Implementação de login, registro e recuperação de senha para usuários, utilizando bibliotecas como Flask-Login e Flask-WTF para gerenciar sessões com segurança.
Diferenciação entre usuários comuns (clientes) e administradores, garantindo que apenas administradores possam gerenciar o catálogo de produtos.

# Gestão de Produtos

Um painel administrativo permite que administradores adicionem, editem ou removam produtos, além de definir categorias e gerenciar inventário.
Cada produto possui atributos como nome, descrição, preço, imagens e quantidade disponível em estoque, armazenados em um banco de dados relacional (por exemplo, SQLite ou PostgreSQL).

# Catálogo e Pesquisa de Produtos

Os clientes podem navegar por uma interface amigável que lista os produtos disponíveis, filtrando por categorias e preços.
A função de busca permite encontrar produtos específicos rapidamente.

# Carrinho de Compras

Clientes podem adicionar e remover produtos do carrinho, alterar quantidades e visualizar um resumo do pedido em tempo real.
O carrinho é armazenado na sessão do usuário e atualizado dinamicamente utilizando AJAX para uma experiência mais fluida.

# Finalização de Compra (Checkout)

Integração com sistemas de pagamento externos (como Stripe ou PayPal) para processar pagamentos de forma segura.
Gestão de endereços de entrega e métodos de envio, com cálculo de frete automatizado.

# Histórico de Pedidos e Rastreamento

Após a compra, o cliente pode visualizar um histórico de pedidos, com detalhes do status de cada pedido e informações de rastreamento de entrega.

# Segurança

O projeto implementa medidas de segurança, como proteção contra ataques CSRF (Cross-Site Request Forgery), XSS (Cross-Site Scripting), e encriptação de senhas utilizando Flask-Bcrypt.

# Escalabilidade

O Flask é configurado para funcionar com servidores de produção, como Gunicorn, e é preparado para escalar horizontalmente, caso a demanda de tráfego aumente.
