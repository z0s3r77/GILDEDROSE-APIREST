import pytest
from repository.MongoAtlasConexion import connect


@pytest.mark.test_db
def test_MongoAtlasConection():
    # Check mongo atlas conection
    assert connect(host="OIhsioahd") == False
    assert connect(host="https://www.mongodb.com/atlas/app-services/data-api") == True
