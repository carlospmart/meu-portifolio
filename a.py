def gerar_clamp(
    min_font: float, 
    max_font: float, 
    min_width: int = 375, 
    max_width: int = 1200, 
    root_size: int = 16
) -> str:
    """
    Gera uma string CSS clamp() fluida e acessível.

    Args:
        min_font (float): Tamanho mínimo da fonte em rem (ex: 2.12).
        max_font (float): Tamanho máximo da fonte em rem (ex: 3).
        min_width (int, optional): Largura mínima da tela em px. Padrão é 375.
        max_width (int, optional): Largura máxima da tela em px. Padrão é 1200.
        root_size (int, optional): Tamanho base do rem em px. Padrão é 16.

    Returns:
        str: A função clamp() formatada para CSS.
    """
    # Converte as larguras de px para rem
    min_width_rem = min_width / root_size
    max_width_rem = max_width / root_size

    # Calcula a inclinação (slope) e a interseção (base em rem)
    slope = (max_font - min_font) / (max_width_rem - min_width_rem)
    y_axis_intersection = -min_width_rem * slope + min_font

    # Calcula os valores finais
    preferred_vw = slope * 100
    sinal = "+" if y_axis_intersection >= 0 else "-"
    base_absoluto = abs(y_axis_intersection)

    # Retorna a string formatada com 2 casas decimais nos cálculos
    return f"clamp({min_font}rem, {base_absoluto:.2f}rem {sinal} {preferred_vw:.2f}vw, {max_font}rem)"

print(gerar_clamp(0.9375,))