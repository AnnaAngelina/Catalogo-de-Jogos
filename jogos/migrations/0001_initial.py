from django.db import migrations, models
import django.db.models.deletion


def cadastrar_dados(apps, schema_editor):
    Desenvolvedora = apps.get_model("jogos", "Desenvolvedora")
    Plataforma = apps.get_model("jogos", "Plataforma")
    Jogo = apps.get_model("jogos", "Jogo")

    desenvolvedoras = {}
    for nome in [
        "Nintendo", "Rockstar Games", "Santa Monica Studio",
        "CD Projekt Red", "Mojang Studios", "FromSoftware"
    ]:
        desenvolvedoras[nome] = Desenvolvedora.objects.create(nome=nome)

    plataformas = {}
    for nome in ["Nintendo Switch", "PlayStation 5", "PC", "Xbox Series X"]:
        plataformas[nome] = Plataforma.objects.create(nome=nome)

    dados = [
        ("The Legend of Zelda: Breath of the Wild", "Uma aventura de mundo aberto em Hyrule, com exploração e liberdade para resolver desafios.", 2017, "Nintendo", "Nintendo Switch"),
        ("Super Mario Odyssey", "Mario viaja por diferentes reinos em uma aventura para resgatar a princesa Peach.", 2017, "Nintendo", "Nintendo Switch"),
        ("Mario Kart 8 Deluxe", "Corridas divertidas com personagens clássicos e pistas variadas.", 2017, "Nintendo", "Nintendo Switch"),
        ("Animal Crossing: New Horizons", "Construa e personalize sua própria ilha em um jogo tranquilo de simulação.", 2020, "Nintendo", "Nintendo Switch"),
        ("Pokémon Legends: Arceus", "Explore a região de Hisui e descubra os primeiros registros da Pokédex.", 2022, "Nintendo", "Nintendo Switch"),
        ("Super Smash Bros. Ultimate", "Personagens de diferentes franquias se enfrentam em batalhas.", 2018, "Nintendo", "Nintendo Switch"),
        ("Red Dead Redemption 2", "Uma história de faroeste em um grande mundo aberto.", 2018, "Rockstar Games", "PlayStation 5"),
        ("Grand Theft Auto V", "Acompanhe três protagonistas em uma cidade cheia de possibilidades.", 2013, "Rockstar Games", "PC"),
        ("Bully", "Uma aventura ambientada em uma escola fictícia e seus arredores.", 2006, "Rockstar Games", "PC"),
        ("God of War Ragnarök", "Kratos e Atreus enfrentam novos desafios inspirados na mitologia nórdica.", 2022, "Santa Monica Studio", "PlayStation 5"),
        ("God of War", "Kratos inicia uma jornada pelos reinos da mitologia nórdica ao lado do filho.", 2018, "Santa Monica Studio", "PC"),
        ("The Witcher 3: Wild Hunt", "Geralt de Rívia procura por Ciri em um mundo de fantasia.", 2015, "CD Projekt Red", "PC"),
        ("Cyberpunk 2077", "Um RPG de mundo aberto ambientado na futurista Night City.", 2020, "CD Projekt Red", "Xbox Series X"),
        ("Minecraft", "Crie, explore e construa mundos usando blocos.", 2011, "Mojang Studios", "PC"),
        ("Minecraft Dungeons", "Uma aventura de ação com exploração de masmorras no universo Minecraft.", 2020, "Mojang Studios", "Nintendo Switch"),
        ("Elden Ring", "Explore Terras Intermédias em um RPG de ação e fantasia.", 2022, "FromSoftware", "PlayStation 5"),
        ("Dark Souls III", "Enfrente inimigos desafiadores em um mundo de fantasia sombria.", 2016, "FromSoftware", "PC"),
        ("Sekiro: Shadows Die Twice", "Um jogo de ação focado em combates e precisão.", 2019, "FromSoftware", "Xbox Series X"),
        ("The Legend of Zelda: Tears of the Kingdom", "Uma nova jornada por Hyrule, agora também explorando os céus e o subterrâneo.", 2023, "Nintendo", "Nintendo Switch"),
        ("Luigi's Mansion 3", "Luigi explora um hotel assombrado para salvar seus amigos.", 2019, "Nintendo", "Nintendo Switch"),
        ("Donkey Kong Country: Tropical Freeze", "Uma aventura de plataforma com desafios em diferentes cenários.", 2014, "Nintendo", "Nintendo Switch"),
        ("Red Dead Redemption", "Uma história de faroeste sobre John Marston.", 2010, "Rockstar Games", "Xbox Series X"),
        ("The Witcher 2: Assassins of Kings", "Geralt se envolve em conflitos políticos e mistérios.", 2011, "CD Projekt Red", "PC"),
        ("Dark Souls Remastered", "Uma versão remasterizada da aventura que iniciou a série Dark Souls.", 2018, "FromSoftware", "PlayStation 5"),
    ]

    for nome, descricao, ano, dev, plataforma in dados:
        Jogo.objects.create(
            nome=nome,
            descricao=descricao,
            ano_lancamento=ano,
            desenvolvedora=desenvolvedoras[dev],
            plataforma=plataformas[plataforma],
        )


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Desenvolvedora",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name": "Desenvolvedora",
                "verbose_name_plural": "Desenvolvedoras",
                "ordering": ["nome"],
            },
        ),
        migrations.CreateModel(
            name="Plataforma",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=60)),
            ],
            options={
                "verbose_name": "Plataforma",
                "verbose_name_plural": "Plataformas",
                "ordering": ["nome"],
            },
        ),
        migrations.CreateModel(
            name="Jogo",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=120)),
                ("descricao", models.TextField()),
                ("ano_lancamento", models.PositiveIntegerField()),
                ("desenvolvedora", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="jogos", to="jogos.desenvolvedora")),
                ("plataforma", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="jogos", to="jogos.plataforma")),
            ],
            options={
                "verbose_name": "Jogo",
                "verbose_name_plural": "Jogos",
                "ordering": ["nome"],
            },
        ),
        migrations.RunPython(cadastrar_dados, migrations.RunPython.noop),
    ]
