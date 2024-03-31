@echo off

for %%r in (constant invscaling adaptive) do (
    for %%h in (50 100 200) do (
        for %%l in (1e-3, 1e-4 1e-5) do (
            for %%a in (1e-6, 1e-7, 1e-8) do (
                for %%i in (50, 100, 200, 500, 1000) do (
                    python main_mlp.py --learning_rate %%r --hidden_layer_sizes %%h --learning_rate_init %%l --alpha %%a --max_iter %%i
                )
            )
        )
    )
)