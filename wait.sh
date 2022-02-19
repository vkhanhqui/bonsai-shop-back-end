while ! nc -z db 3306 ; do
    echo "Waiting for the MySQL Server"
    sleep 3
done


uvicorn app.main:app --host 0.0.0.0 --port 8000