// FORMATAÇÃO E VALIDAÇÃO

// ===== Validação utilizada nas 3 tabelas =====

function validateStrings(value) {
    return typeof value === 'string' && value.trim().length >= 3;
}

// ===== Formatação e Validação para a tabela de CLIENTES =====

function formatPhone(value) {
    const numbers = value.replace(/\D/g, '');
    return numbers.length === 11
        ? numbers.replace(/(\d{2})(\d{5})(\d{4})/, '($1) $2-$3')
        : numbers.replace(/(\d{2})(\d{4})(\d{4})/, '($1) $2-$3');
}

function formatCpfCnpj(value) {
    const digits = value.replace(/\D/g, '');
    if (digits.length <= 11) {
        return digits.replace(/(\d{3})(\d{3})(\d{3})(\d{0,2})/, '$1.$2.$3-$4').replace(/[-.]$/, '');
    } else {
        return digits.replace(/(\d{2})(\d{3})(\d{3})(\d{4})(\d{0,2})/, '$1.$2.$3/$4-$5').replace(/[-./]$/, '');
    }
}

function validateCpfCnpj(value) {
    const numbers = value.replace(/\D/g, '');
    return numbers.length === 11 || numbers.length === 14;
}

function validatePhone(value) {
    const numbers = value.replace(/\D/g, '');
    return numbers.length === 10 || numbers.length === 11;
}

function validateEmail(value) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
}

// ===== Validação para a tabela de EQUIPAMENTOS =====

function validateValorDiaria(value) {
    const parsed = parseFloat(value);
    return !isNaN(parsed) && parsed > 0;
}

// ===== Formatação e Validação para a tabela de RESERVAS =====

function formatDateForInput(dateStr) {
    const date = new Date(dateStr);
    return date.toISOString().split('T')[0];
}

function formatDateToPtBr(dateStr) {
    const [year, month, day] = dateStr.split("-");
    return `${day}/${month}/${year}`;
}

function validateSelect(value) {
    return value !== null && value !== '';
}

function validateDataInicioFim(inicio, fim) {
    const d1 = new Date(inicio);
    const d2 = new Date(fim);
    return d1 instanceof Date && d2 instanceof Date && d1 <= d2;
}

function validateStatus(value) {
    const validStatus = ['Ativa', 'Cancelada', 'Finalizada'];
    return validStatus.includes(value);
}

// EXPORTANDO AS FUNÇÕES

module.exports = {
  validateStrings,
  validateCpfCnpj,
  validateEmail,
  validatePhone,
  validateValorDiaria,
  validateSelect,
  validateDataInicioFim,
  validateStatus,
};
