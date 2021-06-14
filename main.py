import speedtest

def main():
	test = speedtest.Speedtest()

	print("Loading serverlist...")
	test.get_servers() # -> get list of servers
	print("Choosing best server...")
	best = test.get_best_server() # -> choos best server
	print(f"Found: {best['host']} located in {best['country']}")

	print("Performing download test...")
	download_result = test.download()
	print("Performing upload test...")
	upload_result = test.upload()
	ping_result = test.results.ping

	print("===============RESULT================")
	print(f"Download speed: {download_result / 1024 / 1024 * 0.125:.2f} MB/s ({download_result / 1024 / 1024}:.2f Mbit/s)")
	print(f"Upload speed: {upload_result / 1024 / 1024 * 0.125:.2f} MB/s ({upload_result / 1024 / 1024}:.2f Mbit/s)")
	print(f"Ping: {ping_result :.2f} ms")
	print("======================================")
	input("ENTER to finish!!!")

if __name__ == '__main__':
	main()