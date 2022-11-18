# Connecting Github with Jenkins and Dockers

``````ad-abstract
title:

``````
````ad-info
title:process
Despues de instalar tanto Dockers como Jenkins. Se elaboró un programa simple que se subió a Github en un repositorio https://github.com/ErickMontesDK/jenkins-docker.

Para conectar Jenkins a docker, instalamos la imagen de jenkins en docker con el cmd
`docker pull jenkins/jenkins`
Una vez instalada, podemos ver nombre del contenedor con 
	`docker images`
En mi caso, es con el nombre jenkins/jenkins tag=latest
![[Pasted image 20221117192840.png]]

Para ejecutar el contenedor, se ejecuta el comando:
`docker run -p 8080:8080 -p 5000:5000 -d -v jenkins_home:/var/jenkins_home jenkins/jenkins:latest`
![[Pasted image 20221117193507.png]]

Entramos a localhost:8080, donde pide una contraseña para ingresar. La contraseña se obtiene con el siguiente codigo
`docker ps`-->Obtiene el id de nuestro contenedor
`docker exec -i -t <container_id> /bin/bash`--> ingresamos al docker shell. Solo me funcionó el windows powershell, no trabajaba en git bash
`jenkins@<container_id>:/$ cat /var/jenkins_home/secrets/initialAdminPassword`-->Nos da la clave de ingreso

![[Pasted image 20221117195846.png]]

![[Pasted image 20221117195958.png]]

![[Pasted image 20221117200455.png]]

![[Pasted image 20221117200535.png]]

![[Pasted image 20221117200516.png]]

![[Pasted image 20221117200813.png]]

![[Pasted image 20221117200959.png]]
````