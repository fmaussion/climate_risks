fig, ax = plt.subplots()
x_quants = np.linspace(1e-6, 1-1e-6, 101)
ax.plot(stats.norm.ppf(x_quants, 
                       annual_max.mean(),
                       annual_max.std()),
        # quantiles of a normal distribution with the mean and std of our precip data
        np.quantile(annual_max, x_quants),  # quantiles of our precip data
        "o",
        )
ax.plot(x_pdf, x_pdf, "k")

ax.set_xlim(0, annual_max.max() + 5)
ax.set_ylim(0, annual_max.max() + 5)

ax.set_xlabel("Normal Quantiles")
ax.set_ylabel("Sample Quantiles")

ax.grid(True)
ax.set_aspect("equal")