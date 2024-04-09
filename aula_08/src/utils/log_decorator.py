# decorator para registro de logs
from loguru import logger


def log_decorator(func):
    """
    Decorador para registro de chamadas de função com o Loguru.

    Args:
        func (callable): Função a ser decorada.

    Returns:
        callable: Função decorada.
    """

    def wrapper(*args, **kwargs):
        """
        Função interna que envolve a função original e realiza o registro.

        Args:
            *args: Argumentos posicionais passados para a função.
            **kwargs: Argumentos de palavras-chave passados para a função.

        Returns:
            Qualquer: Resultado da função original.

        Raises:
            Exception: Se a função original lançar uma exceção.
        """
        # Registra a chamada da função com os argumentos e palavras-chave
        logger.info(f"Chamando '{func.__name__}' com {args} e {kwargs}")

        try:
            # Chama a função original e captura o resultado
            result = func(*args, **kwargs)
            # Registra o retorno da função
            logger.info(f"'{func.__name__}' retornou {result}")
            return result
        except Exception as e:
            # Registra a exceção se a função original lançar uma exceção
            logger.exception(f"'{func.__name__}' lançou uma exceção: {e}")
            # Propaga a exceção para cima na cadeia de chamadas
            raise

    return wrapper
