CREATE TABLE Linha (
    CodigoLinha numeric(5) not null,
    DescricaoLinha varchar(30) not null,

    constraint PK_LINHA primary key(CodigoLinha),
    constraint CK_LINHA_DESCRICAO check (DescricaoLinha <> '')
);

CREATE TABLE Fornecedor (
    CNPJFornecedor varchar(18) not null,
    razaoSocial varchar(100) not null,

    constraint PK_FORNECEDOR primary key(CNPJFornecedor),
    constraint CK_RAZAOSOCIAL check (razaoSocial <> '')
);

CREATE TABLE Produto (
    CodigoProduto numeric(5) not null,
    Descricao varchar(30) not null,
    Estoque numeric(2) not null,
    CodigoLinha numeric(5) not null,
    CNPJFornecedor varchar(18) not null,

    constraint PK_PRODUTO primary key(CodigoProduto),
    constraint CK_PRODUTO_DESCRICAO check (Descricao <> ''),
    constraint FK_PRODUTO_LINHA foreign key(CodigoLinha)
        references Linha(CodigoLinha),
    constraint FK_PRODUTO_FORNECEDOR foreign key(CNPJFornecedor)
        references Fornecedor(CNPJFornecedor)
);