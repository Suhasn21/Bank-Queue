import random
import queue
import matplotlib.pyplot as plt

def simulate_bank_queue(simulation_time, arrival_rate, service_time):
    customer_queue = queue.Queue()
    waiting_times = []
    queue_lengths = [(0, 0)]  # Record time and queue length as tuples
    
    next_arrival_time = random.expovariate(1.0 / arrival_rate)
    next_service_time = 0
    service_completion_time = float('inf')
    
    current_time = 0
    while current_time < simulation_time or not customer_queue.empty():
        if next_arrival_time < service_completion_time and next_arrival_time <= simulation_time:
            current_time = next_arrival_time
            customer_queue.put(current_time)
            next_arrival_time += random.expovariate(1.0 / arrival_rate)
        elif not customer_queue.empty():
            current_time = service_completion_time
            waiting_times.append(current_time - customer_queue.get())
            service_completion_time = current_time + random.expovariate(1.0 / service_time)
        else:
            break
        
        if customer_queue.empty():
            service_completion_time = float('inf')
        else:
            service_completion_time = min(service_completion_time, current_time + random.expovariate(1.0 / service_time))
        
        queue_lengths.append((current_time, customer_queue.qsize()))
    
    average_waiting_time = sum(waiting_times) / len(waiting_times) if waiting_times else 0
    print(f"Average waiting time: {average_waiting_time:.2f} minutes")
    print(f"Total customers served: {len(waiting_times)}")
    
    # Plotting the queue length over time
    times, lengths = zip(*queue_lengths)
    plt.figure(figsize=(10, 6))
    plt.plot(times, lengths, drawstyle='steps-post')
    plt.title('Queue Length Over Time')
    plt.xlabel('Time (minutes)')
    plt.ylabel('Queue Length')
    plt.grid(True)
    plt.show()

# Parameters
simulation_time = 180  # Simulation time in minutes
arrival_rate = 1  # Average time between arrivals in minutes
service_time = 0.5  # Average service time in minutes

simulate_bank_queue(simulation_time, arrival_rate, service_time)
