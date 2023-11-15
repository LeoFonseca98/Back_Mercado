-- Rascunho Banco de Dados

-- Tabela de Usuarios
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    cpf VARCHAR(100) UNIQUE NOT NULL,
    telefone VARCHAR(25) NOT NULL,
    confirme VARCHAR(255) NOT NULL,
    senha VARCHAR(255) NOT NULL),
    criadoEm TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modificadoEm TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de Endereços dos Usuários
CREATE TABLE enderecos (
    id SERIAL PRIMARY KEY,
    rua VARCHAR(255) NOT NULL,
    bairro VARCHAR(100),
    numero INTEGER UNIQUE NOT NULL,
    cep VARCHAR(15) NOT NULL,
    complemento VARCHAR(255),
    usuario_id INTEGER REFERENCES usuarios(id) ON DELETE CASCADE,
    criadoEm TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- controle --
    modificadoEm TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- controle --
);

-- Tabela de Categorias de Produtos
CREATE TABLE categorias (
    id SERIAL PRIMARY KEY,
    descricao VARCHAR(100) UNIQUE NOT NULL
);


-- Tabela de Produtos
CREATE TABLE produtos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    valor DECIMAL(10, 2) NOT NULL,
    quantidade INTEGER NOT NULL,
    categoria_id INTEGER REFERENCES categorias(id) ON DELETE SET NULL,
    criadoEm TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- controle --
    modificadoEm TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- controle --
);

-- Tabela de Vendas
CREATE TABLE vendas (
    id SERIAL PRIMARY KEY,
    usuario_id INTEGER REFERENCES usuarios(id) ON DELETE SET NULL,
    dataVenda TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modificadoEm TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- controle --
);

-- Tabela de Itens da Venda
CREATE TABLE itensVenda (
    id SERIAL PRIMARY KEY,
    venda_id INTEGER REFERENCES vendas(id) ON DELETE CASCADE,
    produto_id INTEGER REFERENCES produtos(id) ON DELETE SET NULL,
    quantidade INTEGER NOT NULL,
    valorUnitario DECIMAL(10, 2) NOT NULL,
    criadoEm TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- controle --
    modificadoEm TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- controle --
);

-- Tabela de Carrinho de Compras
CREATE TABLE carrinhoCompras (
    id SERIAL PRIMARY KEY,
    usuario_id INTEGER REFERENCES usuarios(id) ON DELETE SET NULL,
    criadoEm TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- controle --
    modificadoEm TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- controle --
);

-- Tabela de Itens do Carrinho
CREATE TABLE itensCarrinho (
    id SERIAL PRIMARY KEY,
    carrinho_id INTEGER REFERENCES carrinho_compras(id) ON DELETE CASCADE,
    produto_id INTEGER REFERENCES produtos(id) ON DELETE SET NULL,
    quantidade INTEGER NOT NULL,
    valor DECIMAL(10, 2) NOT NULL,
    criadoEm TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- controle --
    modificadoEm TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- controle --
);

