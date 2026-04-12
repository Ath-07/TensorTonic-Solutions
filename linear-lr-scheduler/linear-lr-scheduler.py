def linear_lr(step, total_steps, initial_lr, final_lr=0.0, warmup_steps=0) -> float:
    """
    Linear warmup (0→initial_lr) then linear decay (initial_lr→final_lr).
    Steps are 0-based; clamp at final_lr after total_steps.
    """
    # Write code here
    out = 0
    if total_steps == 0 or step > total_steps:
        out = final_lr
    elif step < warmup_steps and step != 0:
        out = (step*initial_lr)/warmup_steps
    elif step >= warmup_steps and step <= total_steps:
        out = final_lr + ((initial_lr-final_lr) * ((total_steps-step)/(total_steps-warmup_steps)))
    else:
        out = 0

    return out
    pass