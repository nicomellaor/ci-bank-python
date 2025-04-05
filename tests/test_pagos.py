
import pytest
from unittest.mock import patch
from src.pagos import procesar_pago

# 1. Saldo mayor que el monto -> True
@patch('src.pagos.verificar_saldo_en_banco')
def test_saldo_mayor(mock_verificar):
    mock_verificar.return_value = 100.0
    resultado = procesar_pago("nicolas012", 50.0, mock_verificar)
    mock_verificar.assert_called_once_with("nicolas012")
    assert resultado is True

# 2. Saldo igual al monto -> True
@patch('src.pagos.verificar_saldo_en_banco')
def test_saldo_igual(mock_verificar):
    mock_verificar.return_value = 50.0
    resultado = procesar_pago("nicolas012", 50.0, mock_verificar)
    mock_verificar.assert_called_once_with("nicolas012")
    assert resultado is True

# 3. Saldo menor que el monto -> False
@patch('src.pagos.verificar_saldo_en_banco')
def test_saldo_menor(mock_verificar):
    mock_verificar.return_value = 30.0
    resultado = procesar_pago("nicolas012", 50.0, mock_verificar)
    mock_verificar.assert_called_once_with("nicolas012")
    assert resultado is False

# 4. Saldo cero o negativo -> False
@patch('src.pagos.verificar_saldo_en_banco')
def test_saldo_cero(mock_verificar):
    mock_verificar.return_value = 0.0
    resultado = procesar_pago("nicolas012", 10.0, mock_verificar)
    mock_verificar.assert_called_once_with("nicolas012")
    assert resultado is False

# 5. Excepción en API
@patch("src.pagos.verificar_saldo_en_banco")
def test_error_de_api(mock_verificar):
    # Configuro el mock para que lance ConnectionError
    mock_verificar.side_effect = ConnectionError("timeout")
    with pytest.raises(ConnectionError):
        procesar_pago("nicolas012", 20.0, mock_verificar)
    mock_verificar.assert_called_once_with("nicolas012")
