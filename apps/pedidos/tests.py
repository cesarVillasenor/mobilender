from django.test import TestCase
from .models import Pedidos


class ModelTestCase(TestCase):

    def test_obtener_ultimos_pedidos_cliente_platino(self):
        """Todos los clientes son de tipo platino"""
        es_cliente_platino = True
        pedidos = Pedidos.obtener_ultimos_pedidos_cliete_platino(self)
        for pedido in pedidos:
            if pedido.Cliente.tipo != 4:
                es_cliente_platino = False
                break
        self.assertEqual(es_cliente_platino, True)


class ViewTestCase(TestCase):

    def test_localhost_carga_apropiadamnete(self):
        """localhost responde apropiadamente"""
        response = self.client.get('http://127.0.0.1:8000')
        self.assertEqual(response.status_code, 200)

    def test_api_carga_apropiadamnete(self):
        """api responde apropiadamente"""
        response = self.client.get('/pedidos/api/')
        self.assertEqual(response.status_code, 200)

    def test_crear_empresa(self):
        data = {
            'referencia': 'Empresa test',
            'codigo': '1',
        }
        response = self.client.post('/pedidos/api/empresas', data)
        self.assertEqual(response.status_code, 200)
