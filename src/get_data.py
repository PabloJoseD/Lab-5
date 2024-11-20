import serial
import csv

# Configure the serial connection
SERIAL_PORT = 'COM10'  # Update with your actual COM port
BAUD_RATE = 9600  # Match the Arduino baud rate

movimiento = input(
                "Indique el numero del movimeito a registrar:\n"
                "1. Estático\n"
                "2. Circular\n"
                "3. Puñetazo\n"
                "4. Flexión \n"
                "5. Arriba y abajo\n\n"
                "Su selección:"
            )

movimiento = int(movimiento)

if movimiento == 1:
    CSV_FILE = 'estatico.csv'
elif movimiento == 2:
    CSV_FILE = 'circular.csv'
elif movimiento == 3:
    CSV_FILE = 'punch.csv'
elif movimiento == 4:
    CSV_FILE = 'flex.csv'
elif movimiento == 5:
    CSV_FILE = 'updown.csv'
else:
    print("El tipo de movimiento no es válido\n")
    exit()

# Open the serial port
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    print(f"Connected to {SERIAL_PORT} at {BAUD_RATE} baud.")
except serial.SerialException as e:
    print(f"Error: {e}")
    exit()

# Open CSV file for writing
with open(CSV_FILE, mode='w', newline='') as file:
    csv_writer = csv.writer(file)

    try:
        while True:
            # Read a line from the serial monitor
            line = ser.readline().decode('utf-8').strip()
            if line:
                print(line)  # Print to console for monitoring
                # Write the raw data as a row in the CSV file
                csv_writer.writerow(line.split(','))
                file.flush()  # Ensure data is written to the file
    except KeyboardInterrupt:
        print("\nStopped by user.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        ser.close()
        print("Serial port closed.")
