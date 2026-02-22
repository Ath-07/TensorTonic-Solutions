def min_max_scaling(data):
    """
    Scale each column of the data matrix to the [0, 1] range.
    """
    # Write code here
    min_val = []
    max_val = []
    for i in range(len(data[0])):
        column = [row[i] for row in data]
        min_val.append(min(column))
        max_val.append(max(column))
    data_scaled = []
    for i in range(len(data)):
        scaled_row = []
        for j in range(len(data[0])):
            # Avoid division by zero
            if max_val[j] == min_val[j]:
                scaled_row.append(0)
            else:
                scaled_row.append(
                    (data[i][j] - min_val[j]) / (max_val[j] - min_val[j])
                )
        data_scaled.append(scaled_row)
    return data_scaled
    