o
    �Q�e�  �                   @   sr   d dl mZ d dlmZ ee�Zdejd< ee�ZG dd� dej�Z	e�
d�dd	� �Zed
kr7ejdd� dS dS )�    )�Flask)�
SQLAlchemyzsqlite:///ecommerce.dbZSQLALCHEMY_DATABASE_URIc                   @   sT   e Zd Zejejdd�Zeje�d�dd�Zejej	dd�Z
eje�d�dd�ZdS )�ProductT)Zprimary_key�2   F)Znullable�x   N)�__name__�
__module__�__qualname__�dbZColumnZInteger�id�String�nameZFloatZprice�description� r   r   �%D:\rocketseat\introPythonFlask\app.pyr      s
    r   �/c                   C   s   dS )NzHello Worldr   r   r   r   r   �hello_world   s   r   �__main__T)�debugN)�flaskr   Zflask_sqlalchemyr   r   �app�configr
   ZModelr   �router   �runr   r   r   r   �<module>   s   

�