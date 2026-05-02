def start_game():
    score = 0
    print("\n" + "="*60)
    print("🎯 RECRUITER SIMULATOR - Edição Profissional")
    print("="*60)
    print("Sua missão: contratar o desenvolvedor certo.\n")

    candidates = {
        "A": {"name": "Alex", "desc": "Fala muito bem, mas entrega pouco.", "result": "Missed opportunity - Falta execução."},
        "B": {"name": "Beatriz", "desc": "Sabe muita teoria, mas nunca colocou em produção.", "result": "Ainda não está pronto."},
        "C": {"name": "Carlos", "desc": "Constrói, entrega, mede resultado e melhora sempre.", "result": "EXCELENTE CONTRATAÇÃO!"}
    }

    for round in range(1, 4):
        print(f"\nRodada {round}/3")
        for key, info in candidates.items():
            print(f"{key} - {info['name']}: {info['desc']}")
        
        choice = input("\nQuem você contrata nessa rodada? (A/B/C): ").strip().upper()
        
        if choice in candidates:
            print(f"\n✅ Você escolheu {candidates[choice]['name']}")
            print(candidates[choice]['result'])
            if choice == "C":
                score += 10
                print("🎉 +10 pontos!")
        else:
            print("\n❌ Escolha inválida. Preste mais atenção.")
        
        print("-" * 40)

    print("\n" + "="*60)
    print("RESULTADO FINAL")
    print("="*60)
    if score >= 25:
        print("🏆 PARABÉNS! Você é um ótimo recrutador.")
        print("Você sabe identificar quem realmente entrega resultado.")
    elif score >= 10:
        print("👍 Bom, mas ainda pode melhorar.")
    else:
        print("⚠️  Precisa treinar mais sua capacidade de julgar execução.")

    print(f"\nSua pontuação final: {score}/30")

    replay = input("\nJogar novamente? (s/n): ").strip().lower()
    if replay == "s" or replay == "sim":
        start_game()

if __name__ == "__main__":
    start_game()