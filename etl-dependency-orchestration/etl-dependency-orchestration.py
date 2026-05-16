def schedule_pipeline(tasks, resource_budget):
    """
    Schedule ETL tasks respecting dependencies and resource limits.
    """
    # Write code here
    completed = set()
    started = set()

    # running = list of: (end_time, task_name, resources)
    running = []
    schedule = []

    current_time = 0
    current_resources = 0
    
    total_tasks = len(tasks)

    while len(completed) < total_tasks:
        # Complete finished tasks
        finished = []

        for task_info in running:
            end_time, task_name, resources = task_info

            if end_time <= current_time:
                finished.append(task_info)

        for end_time, task_name, resources in finished:
            running.remove((end_time, task_name, resources))

            completed.add(task_name)
            current_resources -= resources

        # Find ready tasks
        ready = []

        for task in tasks:
            name = task["name"]

            if name in started:
                continue

            # Check dependencies
            if all(dep in completed for dep in task["depends_on"]):
                ready.append(task)

        # Alphabetical order
        ready.sort(key=lambda x: x["name"])

        # Greedily schedule
        for task in ready:
            needed = task["resources"]

            if current_resources + needed <= resource_budget:
                start_time = current_time
                end_time = start_time + task["duration"]
                running.append((end_time, task["name"], needed))
                started.add(task["name"])
                current_resources += needed
                schedule.append((task["name"], start_time))

        # Advance time to next completion
        if running:
            next_end = min(task[0] for task in running)
            current_time = next_end

    # Sort by (start_time, task_name)
    schedule.sort(key=lambda x: (x[1], x[0]))

    return schedule