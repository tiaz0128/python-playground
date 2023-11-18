from tqdm import tqdm


class ProgressBar:
    def __init__(self, jobs, desc="Processing"):
        self.pbar = tqdm(
            total=len(jobs),
            desc=desc,
            unit="call",
            bar_format="{l_bar}{bar}{n_fmt}/{total_fmt} [{elapsed} {unit}]",
        )

    def __enter__(self):
        return self.pbar

    def __exit__(self, exc_type, exc_value, traceback):
        self.pbar.close()
