def validate_records(records, schema):
    """
    Validate records against a schema definition.
    """
    # Write code here
    type_map = {"int": int, "float": float, "str": str}
    results = []

    for idx, record in enumerate(records):
        errors = []
        for col_schema in schema:
            column = col_schema["column"]
            expected_type = col_schema["type"]
            nullable = col_schema["nullable"]

            if column not in record:
                errors.append(f"{column}: missing")
                continue

            value = record[column]

            if value is None:
                if not nullable:
                    errors.append(f"{column}: null")
                continue

            valid_type = False

            if expected_type == "float":
                valid_type = type(value) in (int, float)
            else:
                valid_type = type(value) is type_map[expected_type]

            if not valid_type:
                errors.append(
                    f"{column}: expected {expected_type}, got {type(value).__name__}"
                )
                continue
                        
            if expected_type in ("int", "float"):
                if "min" in col_schema and value < col_schema["min"]:
                    errors.append(f"{column}: out of range")
                    continue

                if "max" in col_schema and value > col_schema["max"]:
                    errors.append(f"{column}: out of range")
                    continue

        results.append((idx, len(errors) == 0, errors))

    return results