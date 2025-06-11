-- Admin's / Funcionários do sistema 
INSERT INTO `mydb`.`funcionario` (idFuncionario, nomeFuncionario, emailFuncionario, telefoneFuncionario, senhaFuncionario, ehAdmin) VALUES
(1, 'Samuel', 'samu@gmail.com', '12988887777', 'root', 1),
(2, 'Hugo', 'hugo@gmail.com', '35988886666', 'nroot', 0);

-- Populando a tabela cliente
INSERT INTO `mydb`.`cliente` (nomeCliente, emailCliente, telefoneCliente, cpfCnpjCliente) VALUES
('Bruno Ferreira', 'bruno.ferreira@email.com', '11912345678', '123.456.789-10'),
('Juliana Costa', 'juliana.costa@email.com', '11923456789', '987.654.321-00'),
('Carla Martins', 'carla.martins@email.com', '11934567890', '321.654.987-22'),
('Rafael Nogueira', 'rafael.nogueira@email.com', '11945678901', '456.789.123-33'),
('Fernanda Lima', 'fernanda.lima@email.com', '11956789012', '789.123.456-44');

-- Populando a tabela equipamento
INSERT INTO `mydb`.`equipamento` (nomeEquipamento, tipoEquipamento, valorDiaria) VALUES
('Caixa de Som JBL 1000W', 'Som', 120.00),
('Iluminação LED RGB', 'Iluminação', 90.00),
('Tenda 4x4m', 'Estrutura', 150.00),
('Máquina de Fumaça', 'Efeitos Especiais', 70.00),
('Freezer Horizontal 400L', 'Bebidas', 110.00);

-- Populando a tabela reserva
INSERT INTO `mydb`.`reserva` (idCliente, idEquipamento, dataInicio, dataFim, status) VALUES
(1, 1, '2025-06-10', '2025-06-11', 'Ativa'),          -- Bruno reservou caixa de som
(2, 2, '2025-06-08', '2025-06-08', 'Finalizada'),     -- Juliana usou iluminação
(3, 3, '2025-06-15', '2025-06-16', 'Ativa'),          -- Carla reservou tenda
(4, 4, '2025-06-05', '2025-06-05', 'Cancelada'),      -- Rafael cancelou máquina de fumaça
(5, 5, '2025-06-07', '2025-06-09', 'Finalizada');     -- Fernanda usou freezer
