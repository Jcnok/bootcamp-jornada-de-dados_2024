#decorator para registrar o tempo de execução da função em um .csv
import time
import csv
import threading  # Importe o módulo threading aqui

def timer_to_csv(func):
    def format_time(segundos: int): 
        """
        Formata os milisegundos em hora:minuto:segundo
        """
        if segundos < 60:
            return f"{segundos:.3f} segundos"
        elif segundos < 3600:
            minutos, segundos = divmod(segundos, 60)
            return f"{int(minutos)} minutos {int(segundos)} segundos"
        else:
            horas, remainder = divmod(segundos, 3600)
            minutos, segundos = divmod(remainder, 60)
            if minutos == 0:
                return f"{int(horas)} horas {int(segundos)} segundos"
            else:
                return f"{int(horas)} horas {int(minutos)} minutos {int(segundos)} segundos"
    
    def print_elapsed_time(start_time, finished_flag):
        while not finished_flag.is_set():
            elapsed_time = time.time() - start_time
            print(f"Tempo decorrido: {format_time(elapsed_time)}", end="\r")
            time.sleep(1)  # Atualiza a cada segundo

    def wrapper(*args, **kwargs):
        start_time = time.time()
        
        # Inicializa um sinalizador booleano para indicar se a função terminou
        finished_flag = threading.Event()
        
        # Iniciar uma thread para imprimir o tempo decorrido em tempo real
        thread = threading.Thread(target=print_elapsed_time, args=(start_time, finished_flag))
        thread.start()
        
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        print(f"Tempo total de execução: {format_time(elapsed_time)}")
        
        # Sinaliza que a função terminou
        finished_flag.set()
        
        # Salvando o nome da função e o tempo de execução em um arquivo CSV
        with open('data/tempos_execucao.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([func.__name__, format_time(elapsed_time)])
        
        return result    
    return wrapper
