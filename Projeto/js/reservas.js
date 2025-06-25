// CRUD de reservas

let editingReservaId = null;

// Carrega a lista de reservas na tabela
async function loadReservas() {
    const tableBody = document.getElementById('reservasTableBody');
    tableBody.innerHTML = `<tr><td colspan="7"><i class="fas fa-spinner fa-spin me-2"></i>Carregando reservas...</td></tr>`;
    try {
        const reservas = await apiRequest('/reservas');
        if (reservas.length === 0) {
            tableBody.innerHTML = `<tr><td colspan="7" class="text-center">Nenhuma reserva encontrada.</td></tr>`;
            return;
        }
        tableBody.innerHTML = '';
        reservas.forEach(reserva => {
            const dataInicioFormatada = formatDateToPtBr(reserva.dataInicio);
            const dataFimFormatada = formatDateToPtBr(reserva.dataFim);

            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${reserva.idReserva}</td>
                <td>${reserva.nomeCliente}</td>
                <td>${reserva.nomeEquipamento}</td>
                <td>${dataInicioFormatada}</td>
                <td>${dataFimFormatada}</td>
                <td>${reserva.status}</td>
                <td>
                    <button class="btn btn-sm btn-primary" onclick="editReserva(${reserva.idReserva})">Editar</button>
                    <button class="btn btn-sm btn-danger" onclick="deleteReserva(${reserva.idReserva})">Deletar</button>
                </td>`;
            tableBody.appendChild(row);
        });
    } catch (error) {
        tableBody.innerHTML = `<tr><td colspan="7">Erro ao carregar reservas</td></tr>`;
    }
}

// Abre o modal para adicionar uma reserva novo
function showAddReservaModal() {
    editingReservaId = null;
    document.getElementById('reservaModalTitle').textContent = 'Adicionar Reserva';
    document.getElementById('reservaForm').reset();
    new bootstrap.Modal(document.getElementById('reservaModal')).show();
}

// Abre o modal para editar reserva existente
async function editReserva(id) {
    try {
        const reserva = await apiRequest(`/reservas/${id}`);
        editingReservaId = id;
        document.getElementById('reservaModalTitle').textContent = 'Editar Reserva';
        document.getElementById('idClienteReserva').value = reserva.idCliente;
        document.getElementById('idEquipamentoReserva').value = reserva.idEquipamento;
        document.getElementById('dataInicioReserva').value = formatDateForInput(reserva.dataInicio);
        document.getElementById('dataFimReserva').value = formatDateForInput(reserva.dataFim);
        document.getElementById('statusReserva').value = reserva.status;
        new bootstrap.Modal(document.getElementById('reservaModal')).show();
    } catch (error) {
        alert('Erro ao carregar reserva: ' + error.message);
    }
}

// Salva reserva (novo ou editado)
async function saveReserva() {
    const idCliente = document.getElementById('idClienteReserva').value.trim();
    const idEquipamento = document.getElementById('idEquipamentoReserva').value.trim();
    const dataInicio = document.getElementById('dataInicioReserva').value;
    const dataFim = document.getElementById('dataFimReserva').value;
    const status = document.getElementById('statusReserva').value;

    const data = {
        idCliente: idCliente,
        idEquipamento: idEquipamento,
        dataInicio: dataInicio,
        dataFim: dataFim,
        status: status
    };

    try {
        if (editingReservaId) {
            await apiRequest(`/reservas/${editingReservaId}`, 'PUT', data);
            alert('Reserva atualizada com sucesso!');
        } else {
            await apiRequest('/reservas', 'POST', data);
            alert('Reserva adicionada com sucesso!');
        }
        bootstrap.Modal.getInstance(document.getElementById('reservaModal')).hide();
        await loadReservas();
    } catch (error) {
        alert('Erro ao salvar reserva: ' + error.message);
    }
}

// Deleta reserva
async function deleteReserva(id) {
    if (confirm('Deseja excluir esta reserva?')) {
        try {
            await apiRequest(`/reservas/${id}`, 'DELETE');
            alert('Reserva excluída com sucesso!');
            await loadReservas();
        } catch (error) {
            alert('Erro ao excluir reserva: ' + error.message);
        }
    }
}