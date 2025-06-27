import re
from datetime import datetime

# Validações genéricas
def validarString(texto, minLen=1, campo="Campo"):
    if not isinstance(texto, str) or len(texto.strip()) < minLen:
        return f"{campo} deve ter pelo menos {minLen} caracteres."
    return None

def validarEmail(email):
    emailRegex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(emailRegex, email):
        return "Email inválido."
    return None

def validarTelefone(telefone):
    if not isinstance(telefone, str):
        return "Telefone deve ser uma string."

    # Remove caracteres especiais: (, ), espaço, hífen
    telefoneLimpo = re.sub(r'[\s\-\(\)]', '', telefone)

    if not telefoneLimpo.isdigit() or len(telefoneLimpo) not in [10, 11]:
        return "Telefone deve conter 10 ou 11 números, sem caracteres especiais."
    return None

def validarCpfCnpj(cpfCnpj):
    if not isinstance(cpfCnpj, str):
        return "CPF/CNPJ deve ser uma string."

    # Remove pontos, traços e barras
    cpfCnpjLimpo = re.sub(r'[\.\-\/]', '', cpfCnpj)

    if not cpfCnpjLimpo.isdigit() or len(cpfCnpjLimpo) not in [11, 14]:
        return "CPF/CNPJ deve conter 11 ou 14 números, sem pontos, traços ou barras."
    return None

def validarFloat(valor, casasAntes=5, casasDepois=2, campo="Campo"):
    try:
        floatValor = float(valor)
    except (ValueError, TypeError):
        return f"{campo} deve ser um número decimal válido."

    valorStr = f"{floatValor:.{casasDepois}f}"  # garante que terá exatamente 2 casas depois da vírgula
    partes = valorStr.split(".")

    if len(partes[0]) > casasAntes:
        return f"{campo} deve ter no máximo {casasAntes} dígitos antes da vírgula."
    if len(partes[1]) > casasDepois:
        return f"{campo} deve ter no máximo {casasDepois} casas decimais."

    return None

def validarDatas(dataInicioStr, dataFimStr):
    try:
        dataInicio = datetime.strptime(dataInicioStr, "%Y-%m-%d")
        dataFim = datetime.strptime(dataFimStr, "%Y-%m-%d")
    except (ValueError, TypeError):
        return "As datas devem estar no formato YYYY-MM-DD."

    if dataInicio >= dataFim:
        return "A data de início deve ser menor que a data de fim."

    return None

def validarStatus(status, opcoesValidas=["Ativa", "Finalizada", "Cancelada"]):
    if status not in opcoesValidas:
        return f"Status deve ser um dos seguintes: {', '.join(opcoesValidas)}."
    return None

# Validação específica para Cliente
def validarDadosCliente(data):
    erros = []

    if erro := validarString(data.get('nomeCliente', ''), 3, "Nome"):
        erros.append(erro)

    if erro := validarEmail(data.get('emailCliente', '')):
        erros.append(erro)

    if erro := validarTelefone(data.get('telefoneCliente', '')):
        erros.append(erro)

    if erro := validarCpfCnpj(data.get('cpfCnpjCliente', '')):
        erros.append(erro)

    return erros

# Validação específica para Equipamento
def validarDadosEquipamento(data):
    erros = []

    if erro := validarString(data.get('nomeEquipamento', ''), 3, "Nome do Equipamento"):
        erros.append(erro)

    if erro := validarString(data.get('tipoEquipamento', ''), 3, "Tipo do Equipamento"):
        erros.append(erro)

    if erro := validarFloat(data.get('valorDiaria', ''), 5, 2, "Valor da Diária"):
        erros.append(erro)

    return erros

# Validação específica para Reserva
def validarDadosReserva(data, verificarConflito=None):
    erros = []

    if erro := validarDatas(data.get('dataInicio'), data.get('dataFim')):
        erros.append(erro)

    if erro := validarStatus(data.get('status')):
        erros.append(erro)

    # Verifica conflito de reserva se função for passada
    if verificarConflito and data.get('status') == "Ativa":
        conflito = verificarConflito(
            idEquipamento=data['idEquipamento'],
            dataInicio=data['dataInicio'],
            dataFim=data['dataFim']
        )
        if conflito:
            erros.append("Equipamento já reservado nesse período.")

    return erros
