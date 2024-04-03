def exemplo_de_conflito_entre_black_e_flake8():
    variavel_com_nome_muito_longo_para_testar_um_conflito_entre_black_e_flake8 = (
        "conflito"
    )

    if (
        variavel_com_nome_muito_longo_para_testar_um_conflito_entre_black_e_flake8
        == "confito"
    ):
        print("Conflito entre o Black e o Flake8!")
    else:
        print("Sem conflito entre o Black e o Flake8!")

    return variavel_com_nome_muito_longo_para_testar_um_conflito_entre_black_e_flake8


if __name__ == "__main__":
    exemplo_de_conflito_entre_black_e_flake8()
