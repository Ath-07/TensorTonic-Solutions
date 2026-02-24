def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here
    total_num = len(values)
    if max(values) == min(values):
        bin = [0 for i in range(total_num)]
        return bin
    else:
        w = (max(values) - min(values))/num_bins
        bin = []
        for i in values:
            val = int((i - min(values))/w)
            if val < num_bins:
                bin.append(val)
            else:
                bin.append(num_bins-1)
        return bin