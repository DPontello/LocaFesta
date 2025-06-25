//  eventos DOM e inicialização

document.addEventListener('DOMContentLoaded', () => {
    const path = window.location.pathname;

    // Verifica qual página está sendo exibida e chama o carregamento correspondente
    if (path.includes('clientes.html')) {
        loadClientes();
    } else if (path.includes('reservas.html')) {
        loadReservas();
    } else if (path.includes('equipamentos.html')) {
        loadEquipamentos();
    }

    // Validações do formulário de clientes
    const clienteFormHandlers = [
        { input: 'telefoneCliente', format: formatPhone, validate: validatePhone, msg: 'Telefone inválido.' },
        { input: 'emailCliente', validate: validateEmail, msg: 'E-mail inválido.' },
        { input: 'cpfCnpjCliente', format: formatCpfCnpj, validate: validateCpfCnpj, msg: 'CPF ou CNPJ inválido.' }
    ];
    clienteFormHandlers.forEach(({ input, format, validate, msg }) => {
        const el = document.getElementById(input);
        if (el && format) el.addEventListener('input', e => e.target.value = format(e.target.value));
        if (el && validate) el.addEventListener('blur', e => {
            if (e.target.value && !validate(e.target.value)) alert(msg);
        });
    });

    // Submissão de formulários
    const forms = [
        { id: 'clienteForm', handler: saveCliente },
        { id: 'reservaForm', handler: saveReserva },
        { id: 'equipamentoForm', handler: saveEquipamento }
    ];
    forms.forEach(({ id, handler }) => {
        const form = document.getElementById(id);
        if (form) form.addEventListener('submit', e => {
            e.preventDefault();
            handler();
        });
    });
});

// Função para voltar ao painel principal
function navigateToMain() {
    window.location.href = 'painel.html';
}

// Simulação de logout (será implementado futuramente o sistema de login)
function logout() {
    alert('Logout realizado.');
    window.location.href = 'index.html';
}
