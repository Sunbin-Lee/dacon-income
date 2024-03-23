for %%h in (100, 200) do (
    for %%a in (1e-4, 1e-5, 1e-6) do (
        for %%i in (200, 500, 1000) do (
            python main_mlp.py --hidden_layer_sizes %%h --alpha %%a --max_iter %%i
        )
    )

)