CREATE TABLE IF NOT EXISTS compras(
	id SERIAL PRIMARY KEY,
	produto TEXT NOT NULL,
	preco NUMERIC(12,2) NOT NULL,
	local_de_compra TEXT,
	promocao BOOLEAN,
	data_de_compra DATE
);

