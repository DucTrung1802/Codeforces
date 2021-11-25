def main():
    raw_values = input()

    values = raw_values.split()
    values = list(map(int, values))

    number_of_trip = values[0]
    ride_per_combo_ticket = values[1]
    single_ticket_price = values[2]
    combo_ticket_price = values[3]

    price_per_combo_ticket = combo_ticket_price/ride_per_combo_ticket

    if single_ticket_price > price_per_combo_ticket:
        number_of_single_ticket = number_of_trip % ride_per_combo_ticket
        number_of_combo_ticket = int(number_of_trip/ride_per_combo_ticket)

        if number_of_single_ticket*single_ticket_price > combo_ticket_price:
            total_cost = (number_of_combo_ticket+1)*combo_ticket_price
            print(total_cost)
        
        else: 
            total_cost = number_of_single_ticket*single_ticket_price + \
                number_of_combo_ticket*combo_ticket_price
            print(total_cost)

                
    else:
        total_cost = number_of_trip*single_ticket_price

        print(total_cost)


if __name__ == '__main__':
    main()
